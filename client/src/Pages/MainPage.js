import React, {useState, useEffect} from "react";
import { Poke_Card } from "../Componenets/poke_card";

export const MainPage = ()=> {
    
    const [MainPokeData, setMainPokeData] = useState([]);

    useEffect(() => {
        let ignoreStaleRequest = false;
        fetch('/test',{ method: "GET" }, { credentials: "same-origin" })
          .then((response) => {
            if (!response.ok) throw Error(response.statusText);
            return response.json();
          })
          .then((data) => {
            if (!ignoreStaleRequest) {
                
                setMainPokeData(data.pokemon)
            }
          })
          .catch((error) => console.log(error));
        
        return () => {
          ignoreStaleRequest = true;
        };
      }, []);
    
    console.log(MainPokeData);
    // MainPokeData.map((PokeData) => (
    //     console.log(PokeData)
    // ));
    
    let counter = 0;

    return(
        <>  
            <div className="grid-container">
                {MainPokeData.map((PokeData) => (
                    <div key={PokeData.poke_id}>
                        <Poke_Card 
                        pokeid = {PokeData.poke_id}
                        pokename = {PokeData.poke_name}
                        pokeimageurl = {PokeData.poke_image}
                        types = {PokeData.poke_types}
                        />
                    </div>
                ))}
            </div>
        </>
    )
}



// <p>
//     {PokeData.poke_id ? (
//     <Poke_Card 
//         pokeid = {PokeData.poke_id}
//         pokename = {PokeData.poke_name}
//         pokeimageurl = {PokeData.poke_image}
//         types = {PokeData.poke_types}
//     />
//     ) : (
//     <></>
//     )}
// </p>
                    