import { useEffect, useState } from "react";
import "./App.css";
import React from "react";
import { AnimateSpinner } from "./components/spinner";

type Data = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
  years_of_experience: number;
  specialties: string;
  bio: string;
  website: string;
  portfolio: string;
  is_available: boolean;
  location: string;
  created_at: string;
  updated_at: string;
};

function App() {
  const [designers, setDesignerData] = useState<Data[] | undefined>(undefined);

  useEffect(() => {
    fetch("https://unmess.sannty.in/api/designers/")
      .then((response) => response.json())
      .then((data) => setDesignerData(data?.results));
  }, []);

  // if (Array.isArray(designers) && designers.length === 0) {
  //   return <div>No Data Found</div>;
  // }

  function renderSection(heading: string, data: Data[] | undefined) {
    return (
      <>
        <h1>
          {heading} ({designers?.length})
        </h1>
        <section
          style={{
            display: "flex",
            flexDirection: "row",
            justifyContent: "flex-end",
            flexWrap: "wrap",
          }}
        >
          {data?.map((d: Data, i: number) => (
            <div
              key={d.id}
              style={{
                border: "1px dashed black",
                borderRadius: "8px",
                width: "360px",
                margin: "16px",
                padding: "16px",
              }}
            >
              <img
                style={{
                  borderRadius: "20px",
                  height: "200px",
                }}
                src={`/${i + 1}.jpeg`}
                alt={"/${i+1}.jpeg"}
              />
              <h2>{`${d?.first_name} ${d?.last_name}`}</h2>
              <p>{d?.bio?.slice(0, 100)}...</p>
              <p>Years of experience: {d?.years_of_experience}</p>
              <p>Specialities: {d?.specialties}</p>
              <p>
                Website: <a>{d?.website}</a>
              </p>
              <p>Email: {d?.email}</p>
              <p>Available: {d?.is_available}</p>
            </div>
          ))}
        </section>
      </>
    );
  }

  // if (designers == undefined) {
  //   return <AnimateSpinner size={128} color="orange" />;
  // }

  return (
    <React.Fragment>{renderSection("Designers", designers)}</React.Fragment>
  );
}

export default App;
