from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    astronaut = "[REDACTED]"
    planet = "Saturn"
    mission = "Project ORBITAL"

    celestial_data = [{
        'name': 'Earth',
        'type' : 'Terrestrial',
        'moons' : '1',
    },
    {
        'name' : 'Saturn',
        'type' : 'Gas Giant',
        'moons' : '146'
    },
    {
        'name' : 'GJ 15 A b',
        'type' : 'Exoplanet',
        'moons' : '0'
    },
    {
        'name' : 'Tau Ceti',
        'type' : 'Star',
        'moons' : '0'
    }]

    return render_template("index.html", name=astronaut, planet=planet, mission=mission, celestial_data=celestial_data)

@app.route('/about')
def about_page():
    return "ORBITAL is a space exploration and observation platform."

@app.route('/object/<name>')
def object_profile(name):
    observed_objects = ['Earth', 'Mars', 'Venus', 'Saturn']
    discovered = True
    object_name = name.lower()
    return render_template("object.html", observed_objects=observed_objects, object_name=object_name, discovered=discovered)

@app.route('/transmissions/<message>')
def transmission(message):
    if len(message) >= 100:
        return f"The 100th character is: {message[99]}"
    else:
        return f"TRANSMISSION TOO SHORT"

@app.route('/callsign/<name>')
def callsign_converter(name):
    if name.endswith("y"):
        return f"{name[:-1]}iful"
    else:
        return f"{name}y"

@app.route('/missions')
def missions_page():
    astronaut = "[REDACTED]"
    missions = [
        {
            "name" : "Voyager 1",
            "destination" : "Interstellar Space",
            "year" : "1977",
            "status" : "Active"
        },
        {
            "name" : "Voyager 2",
            "destination" : "Interstellar Space",
            "year" : "1977",
            "status" : "Active"
        },
        {
            "name" : "Pioneer 10",
            "destination" : "Jupiter",
            "year" : "1972",
            "status" : "decommissioned"
        }
    ]

    render_template("missions.html", name=astronaut, missions=missions)

app.run(debug=True)