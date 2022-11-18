from flask import request, Blueprint, abort
from website.data.cv import cv_by_Name

bp = Blueprint("cv", __name__, url_prefix="/api/v1/cv")

"""
@bp.route("/by_name/<name>")
def by_name(name):
    cv = cv_by_Name(name)

    # return "Im here!"

    if cv is None:
        flash(f"No CV available for {name}.")
    else:
        return cv
"""


@bp.route("/by_name")
def by_name():

    args = request.args
    name = args.get("name")

    cv = cv_by_Name(name)

    # return "Im here!"

    if cv is None:
        abort(404, description=f"No CV available for {name}")
    else:
        return cv
