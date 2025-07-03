from flask import Blueprint, render_template, request
import json
import markdown
from .gemini_api import generate_recommendation

main = Blueprint("main", __name__)

# JSON verisini oku
with open("app/risk_data.json", encoding="utf-8") as f:
    risk_data = json.load(f)

@main.route("/", methods=["GET", "POST"])
def index():
    result = None
    city = ""
    
    if request.method == "POST":
        city = request.form.get("city")
        if city in risk_data:
            risks = risk_data[city]["risk"]
            raw_result = generate_recommendation(city, risks)
            result = markdown.markdown(raw_result)
        else:
            result = "Bu şehir için elimizde veri bulunmamaktadır."

    return render_template("index.html", result=result, cities=sorted(risk_data.keys()), selected_city=city)
