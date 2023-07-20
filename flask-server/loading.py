import requests
import sqlite3
import urllib3

class Loader:

    def __init__(self, poke_id):
        self.connection = sqlite3.connect('database.db')
        self.cur = self.connection.cursor()
        self.poke_id = poke_id
    
    def Table_Pokemon(self, pokemon_json):
        """Load data from Json into pokemon table"""

        self.poke_id = pokemon_json["id"]
        poke_name = pokemon_json["name"]
        poke_weight = pokemon_json["weight"] # 3.93701 # hectograms to inches        
        poke_height = pokemon_json["height"] # 0.220462 # decimetres to lbs
        poke_base_xp  = pokemon_json["base_experience"]
        
        #* Load into sql
        sql = "INSERT INTO pokemon (poke_ID, poke_name, poke_weight, poke_height, poke_base_xp) VALUES (?, ?, ?, ?, ?)"
        val = (self.poke_id, poke_name, poke_weight, poke_height, poke_base_xp)

        try: 
            self.cur.execute(sql, val)
        except sqlite3.IntegrityError as e: #! Error with data already existing
            print(e)
            # pass
        except sqlite3.OperationalError as e: #! Error finding no database
            print(e)
            print("Probable Fix: May have forgotten to run the bin/create or create_db.py script to connect to sql db")
            exit(1)

        self.connection.commit()

    def Table_type(self, pokemon_json):
        """Load data from Json into type table"""

        poke_type_list = []
        poke_types = pokemon_json["types"]
        # print(poke_types)
        for type in poke_types:
            poke_type_list.append(type["type"]["name"])
        
        #* Load into sql 
        for type in poke_type_list:
            sql = "INSERT INTO type (poke_ID, poke_type) VALUES (?, ?)"
            val = (self.poke_id, type)
            try: 
                self.cur.execute(sql, val)
            except sqlite3.OperationalError as e: #! Error finding no database
                print(e)
                print("Probable Fix: May have forgotten to run the bin/create or create_db.py script to connect to sql db")
                exit(1)

        self.connection.commit()

    def Table_ability(self, pokemon_json):
        """Load data from Json into ability table"""

        poke_abilities_list = []
        poke_abilities = pokemon_json["abilities"]
        # print(poke_abilities)
        for ability in poke_abilities:
            if not ability["is_hidden"]:
                poke_abilities_list.append(ability["ability"]["name"])
        
        #* Load into sql 
        for ability in poke_abilities_list:
            sql = "INSERT INTO abilities (poke_ID, ability) VALUES (?, ?)"
            val = (self.poke_id, ability)
            try: 
                self.cur.execute(sql, val)
            except sqlite3.OperationalError as e: #! Error finding no database
                print(e)
                print("Probable Fix: May have forgotten to run the bin/create or create_db.py script to connect to sql db")
                exit(1)

        self.connection.commit()

    def Table_Stats(self, pokemon_json):
        """Load data from Json into stats table"""

        poke_stats = pokemon_json["stats"]

        poke_HP = poke_stats[0]["base_stat"]
        poke_attack = poke_stats[1]["base_stat"]
        poke_defense = poke_stats[2]["base_stat"]
        poke_special_attack = poke_stats[3]["base_stat"]
        poke_special_defense = poke_stats[4]["base_stat"]
        poke_speed = poke_stats[5]["base_stat"]
        
        #* Load into sql 

        sql = "INSERT INTO stats (poke_ID, HP, attack, defense, special_attack, special_defense, speed) VALUES (?, ?, ?, ?, ?, ?, ?)"
        val = (self.poke_id, poke_HP, poke_attack, poke_defense, poke_special_attack, poke_special_defense, poke_speed)
        try: 
            self.cur.execute(sql, val)
        except sqlite3.IntegrityError as e: #! Error with data already existing
            print(e)
            # pass
        except sqlite3.OperationalError as e: #! Error finding no database
            print(e)
            print("Probable Fix: May have forgotten to run the bin/create or create_db.py script to connect to sql db")
            exit(1)

        self.connection.commit()

    def Table_Image(self, pokemon_json):
        """Load images from Json url into the static/uploads folder and 
            saves a path to these locally saved images in the images table"""

        image_url = pokemon_json["sprites"]["other"]["official-artwork"]["front_default"]
        image = requests.get(image_url).content
        file_name = f"static/uploads/pokepic{self.poke_id}.png"

        with open(file_name, 'wb') as handler:
            handler.write(image)

        sql = "INSERT INTO image (poke_ID, poke_image_url) VALUES (?, ?)"
        val = (self.poke_id, file_name)
        try: 
            self.cur.execute(sql, val)
        except sqlite3.IntegrityError as e: #! Error with data already existing
            print(e)
            # pass
        except sqlite3.OperationalError as e: #! Error finding no database
            print(e)
            print("Probable Fix: May have forgotten to run the bin/create or create_db.py script to connect to sql db")
            exit(1)

        self.connection.commit()
    
    #TODO Table_gender(self, pokemon_json):

    #TODO Table_strengths(self, pokemon_json):

    #TODO Table_weaknesses(self, pokemon_json):

def main():
    connection = sqlite3.connect('database.db')
    # cur = connection.cursor()
    

    for i in range(1, 10 ):
        pokemon_request = f"https://pokeapi.co/api/v2/pokemon/{i}"
        response = requests.get(pokemon_request)
        pokemon = response.json()
        loader = Loader(i)
        loader.Table_Pokemon(pokemon_json = pokemon)
        loader.Table_type(pokemon_json = pokemon)
        loader.Table_ability(pokemon_json = pokemon)
        loader.Table_Stats(pokemon_json = pokemon)
        loader.Table_Image(pokemon_json = pokemon)
        

    # for i in range(1, 10):
    #     pokemon_request = f"https://pokeapi.co/api/v2/gender/{i}/"
    #     response = requests.get(pokemon_request)
    #     gender = response.json()
        
        

        
        
    #From Pokemon/
    #https://pokeapi.co/api/v2/pokemon/{id or name}/
        # Load Base Experience, Int (The base experience gained for defeating this Pokémon.)
        # Loading Height, Int ( The height of this Pokémon in decimetres.)
        # Loading ID, Int ( The identifier for this resource.)
        # Loading Name, String ( The name for this resource.)
        # Loading Weight, Int ( The weight of this Pokémon in hectograms.)
        # Loading Abilities, List ( A list of abilities this Pokémon could potentially have.)
            #
        # Loading types, List ( A list of details showing types this Pokémon has.)
            #
        # Loading Stats, List ( A list of base stat values for this Pokémon.)
            #
        # Loading Sprite/Picture of the pokemon
            #

        
    #From Gender/ 
    # https://pokeapi.co/api/v2/gender/{id or name}/
        # Load the Gender


    # How to load
        # Category
        # Weaknesses
        # Strengths
        # Color of Pokemon

    # Additional
        # Should we load verisons?
        # Should we load the other styles of the same pokemon? ex Charizard and Mega Charizard X
        # Should we load Evolution of the pokemon?
    
    
    connection.close()
    return 0

if __name__=="__main__":

    main()

# import requests


# def main():
#    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
# #    print(response.json())
#    json = response.json()
#    print(json["height"])

# if __name__ == "__main__":
#     main()