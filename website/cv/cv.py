from flask import request, Blueprint, abort
from .controller import get_cv_by_Name

bp = Blueprint("cv_bp", __name__, template_folder="templates")


@bp.route("/by_name")
def by_name():

    args = request.args
    name = args.get("name")

    cv = get_cv_by_Name(name)

    # return "Im here!"

    if cv is None:
        abort(404, description=f"No CV available for {name}")
    else:
        return cv
