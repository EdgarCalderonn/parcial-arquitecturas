from model import *
from controller import app
from flask import Flask,render_template,request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/log")
def log():
    tiempo      = request.args.get("tiempo")
    temperatura = request.args.get("temperatura")
    humedad     = request.args.get("humedad")

    if (Modelo.writeData(tiempo,temperatura,humedad)):
        return render_template("mensaje.html",mensaje="Se creo el registro con exito")

    else:
        return render_template("mensaje.html",mensaje="Error al crear el registro")