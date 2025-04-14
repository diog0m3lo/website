from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")

@main.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")