PRAGMA foreign_keys = ON;

CREATE TABLE pokemon(
    poke_ID INTEGER, 
    poke_name TEXT, 
    poke_weight REAL,
    poke_height REAL,
    poke_category TEXT,
    poke_image TEXT,
    PRIMARY KEY(poke_ID)
);

CREATE TABLE type(
    poke_ID INTEGER,
    -- poke_name TEXT,
    poke_type TEXT,


    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE Abilities(
    ability TEXT,
    color TEXT,
    -- poke_name TEXT, 
    poke_ID INTEGER,
    
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE weaknesses(
    weakness TEXT,
    color TEXT,
    -- poke_name TEXT, 
    poke_ID INTEGER,
    
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE Stats(
    HP INTEGER,
    attack INTEGER,
    defense INTEGER,
    special_defense INTEGER,
    special_attack INTEGER,
    speed INTEGER,
    poke_ID INTEGER,
    -- poke_name TEXT,

    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID),
    PRIMARY KEY(poke_ID)
);