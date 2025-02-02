from flask import Blueprint, render_template

bp = Blueprint("quiz", __name__)


@bp.route("/quiz")
def index():
    return render_template("quiz/index.html")


@bp.route("/quiz/generate", methods=["POST"])
def generate():
    return "Generate a quiz"
