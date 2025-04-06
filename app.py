from flask import Flask, request, make_response
from utils import  normalize_name



app = Flask(__name__)


@app.route("/")
def index():
    if request.method == "GET":
        return "Hello, World!"
    return "Hello"

@app.route("/normalize-name", methods=["POST"])
def normalize():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "")
        country = data.get("country", "")
        if not name or not country:
            return make_response("Missing name or country", 400)
        normalized_name = normalize_name(name, country)
        response = make_response(normalized_name)

        return response, 200
    
    return make_response("Invalid request method", 405)

