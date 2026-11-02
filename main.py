from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    astronaut = "Lia"
    planet = "Saturn"
    mission = "Project ORBITAL"

    return render_template("index.html", name=astronaut, planet=planet, mission=mission)

@app.route('/about')
def about_page():
    return "ORBITAL is a space exploration and observation platform"

app.run(debug=True)