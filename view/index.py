# -*- coding: utf-8 -*-

from Run import app
from flask import  url_for
from flask import render_template



@app.route("/")
@app.route("/index")
def index():
    filepath = url_for("static", filename='css/style.css')
    
    return render_template("main/index.html")
