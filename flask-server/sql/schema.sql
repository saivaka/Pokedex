PRAGMA foreign_keys = ON;

CREATE TABLE pokemon(
    poke_ID INTEGER, 
    poke_name TEXT, 
    poke_weight REAL,
    poke_height REAL,
    poke_base_xp INTEGER,
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

CREATE TABLE weaknesses(
    poke_ID INTEGER,
    weakness TEXT,
    
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE gender(
    poke_ID INTEGER,
    gender TEXT,
    
    PRIMARY KEY(poke_ID),
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);


CREATE TABLE image(
    poke_ID INTEGER,
    poke_image TEXT,
    
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

    

CREATE TABLE stats(
    HP INTEGER,
    attack INTEGER,
    defense INTEGER,
    special_defense INTEGER,
    special_attack INTEGER,
    speed INTEGER,
    poke_ID INTEGER,
    -- poke_name TEXT,
    PRIMARY KEY(poke_ID),
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);