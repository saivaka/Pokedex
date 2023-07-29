import React from "react";

export const Poke_Card = ({pokeid, pokename, pokeimageurl, types })=> {
    
    return (
        <div className="poke-box">
            {/* Load Image */}
            <a href={"/pokepage/{{poke.poke_id}}/"}>
                <img src={pokeimageurl} alt= {`image of ${pokename}`}/>
            </a>

            {/* Load Id */}
            <div className = "poke_id">
                #{pokeid}
            </div>   

            {/* Load Name */}
            <div className="poke_name">
                {pokename}
            </div>

            {<div className="poke_types">
                {types.map((type) => ( 
                    <span key={type}>
                        {type}{" "}
                    </span>
                ))}
            </div> }
        </div>
    
    )
}

