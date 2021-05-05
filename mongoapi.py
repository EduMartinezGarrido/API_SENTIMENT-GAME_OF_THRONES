from flask import Flask, request, jsonify
import tools.getdata as get
import json
import markdown.extensions.fenced_code
import tools.postdata as pos

app = Flask(__name__)



@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown(
        readme_file.read(), extensions = ["fenced_code"]

    )
    return md_template

@app.route("/name")
def names():
    nombre = get.personaje_names()
    return jsonify(nombre)


@app.route("/frases/<name>")
def frasesporcentaje(name):
    frases = get.mensajespersonaje(name)
    return jsonify(frases)

@app.route("/frases/<season>/<name>")
def temporadasname(season,name):
    frases = get.temporadas(season,name)
    return jsonify(frases)

@app.route("/nuevafrase", methods=["POST"])
def insertafrase():
    fecha =  request.form.get("Release Date")
    temporada = request.form.get("Season")
    episodio = request.form.get("Episode")
    tituloepisodio = request.form.get("Episode Title")
    nombre = request.form.get("Name")
    frase = request.form.get("Sentence")
    pos.insertafrase(fecha,temporada,episodio,tituloepisodio,nombre,frase)
    return "Se ha introducido el mensaje en la base de datos"

@app.route("/basedatos")
def database():
    basedato = get.base_datos()
    return jsonify(basedato)
    













app.run("0.0.0.0", 5000, debug = True)