from flask import request
from flask import Blueprint


bp = Blueprint("storage", __name__, url_prefix="/")


@bp.route("/", methods=["GET", "POST", "PUT"])
def index():
    if request.method == "GET":
        print("timeout:", request.form['timeout'])
        return "test down URL"
    if request.method == "PUT":
        print("asset uuid:", request.form["asset_uuid"])
        return "done"
    if request.method == "POST":
        print("data type:", request.form["data_type"])
        if request.form["data_type"] != "image":
            return "not supported"
        return "test up URL"
