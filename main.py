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
        'moons' : '1'
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
    return "ORBITAL is a space exploration and observation platform"

@app.route('/object/<name>')
def object_profile(name):
    return f"Welcome to the {name} profile."

app.run(debug=True)