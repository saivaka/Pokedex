PRAGMA foreign_keys = ON;

CREATE TABLE pokemon(
    poke_ID INTEGER, 
    poke_name TEXT, 
    poke_weight REAL,
    poke_height REAL,
    poke_base_xp REAL,
    PRIMARY KEY(poke_ID)
);

CREATE TABLE type(
    poke_ID INTEGER,
    poke_type TEXT,

    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE abilities(
    poke_ID INTEGER,
    ability TEXT, 
    
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE strengths(
    poke_ID INTEGER,
    strengths TEXT,
    
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE weaknesses(
    poke_ID INTEGER,
    weakness TEXT,
    
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE gender(
    poke_name INTEGER,
    gender TEXT,
    
    FOREIGN KEY(poke_name) REFERENCES pokemon(poke_name)
);


CREATE TABLE image(
    poke_ID INTEGER,
    poke_image_url TEXT,
    
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE stats(
    poke_ID INTEGER,
    HP REAL,
    attack REAL,
    defense REAL,
    special_attack REAL,
    special_defense REAL,
    speed REAL,
    -- poke_name TEXT,
    PRIMARY KEY(poke_ID),
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);