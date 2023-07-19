from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__) 



@app.route("/")
def index():
    connection = sqlite3.connect('database.db')
    cur = connection.execute(
        "SELECT poke_ID, poke_name, poke_image_url "
        "FROM pokemon "
    )
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

        poke_dict = {
            "poke_id": poke[0],
            "poke_name": poke[1],
            "poke_image" : poke[2],
            "poke_types" : type_list
        }
        my_poke_list.append(poke_dict)    

    

    context = {"pokemon": my_poke_list}  
    return render_template("index.html", **context)

@app.route("/pokepage/<pokeid_slug>/")
def pokemon(pokeid_slug):
    connection = sqlite3.connect('database.db')
    cur = connection.execute(
        "SELECT * "
        "FROM pokemon "
        "WHERE poke_ID == ? ",
        (pokeid_slug, )
    )
    pokemon = cur.fetchone()

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

    print(poke_type)
    poke_dict = {
        "poke_id": pokemon[0],
        "poke_name": pokemon[1],
        "poke_weight": pokemon[2],
        "poke_height": pokemon[3],
        "poke_base_xp": pokemon[4],
        "types": poke_type_list,
        "abilities": poke_ability_list,
        "image" : pokemon[8]
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
