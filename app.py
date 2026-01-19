# © The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder=".")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logo.png")
def serve_logo():
    return send_from_directory('.', 'logo.png')