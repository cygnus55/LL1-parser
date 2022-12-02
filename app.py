from flask import Flask, render_template, redirect, url_for, request

# from parse_table_generator import table
from left_recursion import left_recursion
from left_factoring import left_factor

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        grammar = request.form.get("grammar")
        left_recursion_free_grammar = left_recursion(grammar[:])
        left_factored_grammar = left_factor(left_recursion_free_grammar[:])
        return render_template("index.html", 
            left_recursion_free_grammar=left_recursion_free_grammar, 
            left_factored_grammar=left_factored_grammar)
    return render_template("index.html")