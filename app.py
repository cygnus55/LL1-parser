from flask import Flask, render_template, redirect, url_for, request

# from parse_table_generator import table
from left_recursion import left_recursion
from left_factoring import left_factor
from first_n_follow import get_first, get_follow, prepare_grammar

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        grammar = request.form.get("grammar")
        if grammar.strip():
            left_recursion_free_grammar = left_recursion(grammar)
            left_factored_grammar = left_factor(left_recursion_free_grammar[:])
            a, b, c, non_terminals, terminals = prepare_grammar(left_factored_grammar)

            first = {}
            follow = {f"{non_terminals[0]}" : {'$'}}

            for each_non_terminal in non_terminals:
                get_first(each_non_terminal, first, c, terminals, non_terminals)

            get_follow(follow, c, terminals, non_terminals, first)

            return render_template("index.html",
                left_recursion_free_grammar=left_recursion_free_grammar,
                left_factored_grammar=left_factored_grammar,
                grammar_body=grammar.strip(),
                first=first,
                follow=follow,
                terminals=terminals,
                non_terminals=non_terminals)
        else:
            return redirect(url_for("index"))
    return render_template("index.html")
