from flask import Flask, render_template, request
from models import PlanetModel, Discovery, PhilosophicSchool

app = Flask(__name__)

planets = [
        PlanetModel("Mercury", "Smallest planet, closest to the Sun", 0),
        PlanetModel("Venus", "Hottest planet with a thick atmosphere", 0),
        PlanetModel("Earth", "Only known planet with life", 1),
        PlanetModel("Mars", "The Red Planet", 2),
        PlanetModel("Jupiter", "Largest planet, gas giant", 95),
        PlanetModel("Saturn", "Gas giant with prominent rings", 146),
        PlanetModel("Uranus", "Ice giant with tilted axis", 27),
        PlanetModel("Neptune", "Farthest planet, strong winds", 14)
    ]
discoveries = [
    Discovery(planets[0], -3000),
    Discovery(planets[1], -3000),
    Discovery(planets[2], -3000),
    Discovery(planets[3], -3000),
    Discovery(planets[4], 1610),
    Discovery(planets[5], 1610),
    Discovery(planets[6], 1781),
    Discovery(planets[7], 1846)
]

schools = [
    PhilosophicSchool("Stoicism"),
    PhilosophicSchool("Epicureanism"),
    PhilosophicSchool("Skepticism")
]


@app.route("/planets")
def planets_route():
    return render_template("planets.html", planets=planets)

@app.route("/quotes")
def quotes_route():
    quotes = {
        "Socrates": "Know thyself.",
        "Plato": "The beginning is the most important part of the work.",
        "Aristotle": "Happiness depends upon ourselves.",
        "Descartes": "I think, therefore I am.",
        "Nietzsche": "He who has a why to live can bear almost any how."
    }
    return render_template("quotes.html", quotes=quotes)

@app.route("/favorite_celestial")
def favorite_celestial_form():
    return render_template("celestial_form.html")

@app.route("/favorite_celestial", methods=["POST"])
def favorite_celestial_response():
    name = request.form["celestial_name"]

    if not name:
        return render_template("celestial_form.html", celestial_name_message = True)

    return f"<h1>Your favorite celestial body is {name}! </h1>"

@app.route("/discoveries")
def discoveries_route():
    return render_template("discoveries.html", discoveries=discoveries)

@app.route("/philosophy_quiz")
def philosophy_quiz_form():
    return render_template("philosophy_quiz.html", philosophy_schools = schools)

@app.route("/philosophy_quiz", methods=["POST"])
def philosophy_quiz_response():
    school_id = request.form["philosophy_id"]
    if not school_id:
        return render_template("philosophy_quiz.html", philosophy_schools = schools, message = "Please select a school.")

    philosophySchool: list[PhilosophicSchool] = list(filter(lambda s: s.Id == int(school_id), schools))

    if not philosophySchool:
        return "<h1>School not found</h1>"

    return f"<h1>You chose {philosophySchool[0].SchoolName}</h1>"


if __name__ == "__main__":

    app.run(debug=True)