from flask import request, Blueprint, abort, render_template
from .controller import get_cv_by_Name

bp = Blueprint("cv", __name__, template_folder="templates")


@bp.route("/")
def index():
    name = "Jakob Kisiala"
    cv = get_cv_by_Name(name)

    return render_template("cv/view.html", cv=cv)
