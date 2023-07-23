from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__) 

@app.route("/")
def index():
    connection = sqlite3.connect('database.db')

    
    if request.args.get('name'):
        cur = connection.execute(
            "SELECT poke_ID, poke_name, poke_image_url "
            "FROM pokemon "
            "WHERE poke_name == ? ",
            (request.args.get('name').capitalize(), )
        )

    else: 
        cur = connection.execute(
            "SELECT poke_ID, poke_name, poke_image_url "
            "FROM pokemon "
        )

        
    #TODO better discription / add comments
    
    # cur = connection.execute(
    #     "SELECT poke_ID, poke_name, poke_image_url "
    #     "FROM pokemon "
    # )
    pokemon = cur.fetchall()
    my_poke_list = []
    # print(pokemon)
    for poke in pokemon:

        cur2 = connection.execute(
            "SELECT poke_type "
            "FROM type "
            "WHERE poke_ID == ? ",
            (poke[0] ,)
        )
        types = cur2.fetchall()
        
        type_list = []
        for type in types:
            type_list.append(type[0])

        # f"{poke[0]:04d}"
        poke_dict = {
            "poke_id": f"{poke[0]:04d}",
            "poke_name": poke[1],
            "poke_image" : poke[2],
            "poke_types" : type_list
        }
        my_poke_list.append(poke_dict)    

    

    context = {"pokemon": my_poke_list}  
    return render_template("index.html", **context)




@app.route("/pokepage/<pokeid_slug>/")
def pokemon(pokeid_slug):
    #TODO better discription / add comments
    connection = sqlite3.connect('database.db')

    # Pull data from pokemon table
    cur = connection.execute(
        "SELECT * "
        "FROM pokemon "
        "WHERE poke_ID == ? ",
        (pokeid_slug, )
    )
    poke_data = cur.fetchone()

    # Pull data from type table
    cur2 = connection.execute(
        "SELECT poke_type "
        "FROM type "
        "WHERE poke_ID == ? ",
        (pokeid_slug, )
    )
    poke_type = cur2.fetchall()
    poke_type_list = []
    for type in poke_type:
        poke_type_list.append(type[0])

    # Pull data from ability table
    cur3 = connection.execute(
        "SELECT ability "
        "FROM abilities "
        "WHERE poke_ID == ? ",
        (pokeid_slug, )
    )
    poke_ability = cur3.fetchall()
    poke_ability_list = []
    for ability in poke_ability:
        poke_ability_list.append(ability[0])

    # Pull data from gender table
    cur4 = connection.execute(
        "SELECT gender "
        "FROM gender "
        "WHERE poke_name == ? ",
        (poke_data[1], )
    )
    genders = cur4.fetchall()
    poke_gender = ""
    #TODO find a better way to depict genders in the pokepage
    if len(genders) == 2:
        poke_gender = "Male + Female"
    elif genders[0][0] == "female":
        poke_gender = "Female"
    elif genders[0][0] == "male":
        poke_gender = "Male"
    else:
        poke_gender = "Genderless"

    # Pull data from stats table
    cur5 = connection.execute(
        "SELECT * "
        "FROM stats "
        "WHERE poke_ID == ? ",
        (pokeid_slug, )
    )
    poke_stats = cur5.fetchone()

    
    poke_dict = {
        "poke_id": f"{poke_data[0]:04d}",
        "poke_name": poke_data[1],
        "poke_weight": poke_data[2],
        "poke_height": poke_data[3],
        "poke_base_xp": poke_data[4],
        "poke_color": poke_data[5],
        "poke_shape": poke_data[6],
        "poke_habitat": poke_data[7],
        "image" : poke_data[8],

        "types": poke_type_list,

        "abilities": poke_ability_list,

        "Gender": poke_gender,
        
        "poke_hp" : poke_stats[1],
        "poke_attack" : poke_stats[2],
        "poke_defense" : poke_stats[3],
        "poke_special_attack" : poke_stats[4],
        "poke_special_defense" : poke_stats[5],
        "poke_speed" : poke_stats[6]
    }

    
    context = {"pokemon": poke_dict}  
    return render_template("pokepage.html", **context)



@app.route("/pokemon")
def pokemon_api():
    connection = sqlite3.connect('database.db')

    cur = connection.execute(
        "SELECT * "
        "FROM pokemon "
    )
    # print(cur)
    pokemon = cur.fetchall()
    # print(pokemon)
    

    context = {"pokemon": pokemon}

    # print(context)
    return jsonify(context)


if __name__ == "__main__":
    app.run(debug=True)
