import requests
import sqlite3



def main():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    for i in range(1, 10):
        pokemon_request = f"https://pokeapi.co/api/v2/pokemon/{i}"
        response = requests.get(pokemon_request)
        pokemon = response.json()
        
        #* Table pokemon
        poke_id = pokemon["id"]
        poke_name = pokemon["name"]
        poke_weight = pokemon["weight"] # 3.93701 # hectograms to inches        
        poke_height = pokemon["height"] # 0.220462 # decimetres to lbs
        poke_base_xp  = pokemon["base_experience"]
        

        #* Load into sql 
        sql = "INSERT INTO pokemon (poke_ID, poke_name, poke_weight, poke_height, poke_base_xp) VALUES (?, ?, ?, ?, ?)"
        val = (poke_id, poke_name, poke_weight, poke_height, poke_base_xp)

        try: 
            cur.execute(sql, val)
        except sqlite3.IntegrityError as e: #! Error with data already existing
            print(e)
        except sqlite3.OperationalError as e: #! Error finding no database
            print(e)
            print("Probable Fix: May have forgotten to run the bin/create or create_db.py script to connect to sql db")
            exit(1)

        connection.commit()

        #? Debug
        # print(poke_id, " ", poke_name, " ", poke_weight, " ", poke_height, " ",  poke_base_xp)
        # data_debug = cur.execute('SELECT * FROM pokemon')
        # print(data_debug.fetchall())

        

        #* Table type 
        poke_type_list = []

        poke_types = pokemon["types"]
        # print(poke_types)
        for type in poke_types:
            poke_type_list.append(type["type"]["name"])
        
        #TODO Load into sql 

        #? Debug
        # for type in poke_type_list:
        #     print(type)
        # print()

        

        #* Table Abilities
        poke_abilities_list = []

        poke_abilities = pokemon["abilities"]
        # print(poke_abilities)
        for ability in poke_abilities:
            if not ability["is_hidden"]:
                poke_abilities_list.append(ability["ability"]["name"])
                

        #TODO Load into sql 

        #? Debug
        # print(poke_abilities_list)
        # print()



        
        #* stats
        
        poke_stats = pokemon["stats"]
        # print(poke_stats)

        poke_HP = poke_stats[0]["base_stat"]
        poke_attack = poke_stats[1]["base_stat"]
        poke_defense = poke_stats[2]["base_stat"]
        poke_special_defense = poke_stats[3]["base_stat"]
        poke_special_attack = poke_stats[4]["base_stat"]
        poke_speed = poke_stats[5]["base_stat"]
        

        #TODO Load into sql 

        #? debug
        # print(poke_HP, poke_attack, poke_defense, poke_special_defense, poke_special_attack, poke_speed)
        # print()



        

        
        
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

    # for i in range(1, 1011):
    #     pokemon_request = f"https://pokeapi.co/api/v2/gender/{i}/"
    #     response = requests.get(pokemon_request)
    #     pokemon = response.json()
        
    #From Gender/ 
    # https://pokeapi.co/api/v2/gender/{id or name}/
        # Load the Gender


    # How to load
        # Category
        # Gender
        # Weaknesses
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