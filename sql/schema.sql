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

    PRIMARY KEY(poke_ID),
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE abilities(
    ability TEXT, 
    poke_ID INTEGER,
    
    PRIMARY KEY(poke_ID),
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE weaknesses(
    weakness TEXT,
    poke_ID INTEGER,
    
    PRIMARY KEY(poke_ID),
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);

CREATE TABLE gender(
    gender TEXT,
    poke_ID INTEGER,
    
    PRIMARY KEY(poke_ID),
    FOREIGN KEY(poke_ID) REFERENCES pokemon(poke_ID)
);


CREATE TABLE image(
    poke_image TEXT,
    poke_ID INTEGER,
    
    PRIMARY KEY(poke_ID),
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