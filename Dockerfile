# syntax=docker/dockerfile:experimental
FROM python:3.12-slim

# Standard recommendation for Python Docker Images
ENV PYTHONDONTWRITEBYTECODE=0
ENV PYTHONUNBUFFERED=0
ENV MAKEFLAGS=-j2

# Create the user
# Ref: https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user
# We install all dependencies together as the later half of the image lacks root access
RUN apt-get update && apt-get dist-upgrade --yes && \
    apt-get install --yes build-essential python3-dev libpq-dev libgdal-dev git openssh-client && \
    apt-get autoremove --yes && apt-get autoclean --yes && apt-get clean && pip install poetry

ARG USERNAME=anton
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    chown -R $USER_UID:$USER_GID /home/$USERNAME


WORKDIR /home/$USERNAME/code

COPY --chown=$USER_UID:$USER_GID pyproject.toml /home/$USERNAME/code/

# Install dependencies
RUN --mount=type=ssh mkdir -m 0644 -p ~/.ssh && \
    ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts && \
    chown -R $USER_UID:$USER_GID /home/$USERNAME && \
    python3 -m venv /home/$USERNAME/.local && . /home/$USERNAME/.local/bin/activate && \
    poetry install --no-root

USER $USERNAME
ENV PATH "$PATH:/home/$USERNAME/.local/bin"
# We want to build with closest to production environment as possible
ARG DJANGO_DEBUG=FALSE

# Dummy credentials for build only!
ENV DJANGO_SETTINGS_MODULE=app.settings \
    DJANGO_DEBUG=${DJANGO_DEBUG} \
    CSRF_TRUSTED_ORIGINS=http://localhost:5173/

COPY  --chown=$USER_UID:$USER_GID . /home/$USERNAME/code/
# RUN . /home/$USERNAME/.local/bin/activate && \
#     poetry run prospector -X --profile-path ./prospector.yaml --max-line-length 120
ENV PYTHONOPTIMIZE=2
# RUN . /home/$USERNAME/.local/bin/activate && \
#     poetry run python manage.py collectstatic --noinput
ENTRYPOINT . /home/$USERNAME/.local/bin/activate && gunicorn app.wsgi --bind=0.0.0.0:8000 --workers=2 -k gevent --log-file=- --access-logfile=-