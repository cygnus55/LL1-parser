from flask import Flask, render_template, redirect, url_for

from parse_table_generator import table

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", table=table)
