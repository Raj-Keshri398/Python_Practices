from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        day = int(request.form["day"])
        month = int(request.form["month"])
        year = int(request.form["year"])
        hour = int(request.form["hour"])
        minute = int(request.form["minute"])

        user_date = datetime(year, month, day, hour, minute)
        now = datetime.now()

        difference = now - user_date

        result = {
            "user_date": user_date.strftime("%d-%m-%Y %H:%M"),
            "current_date": now.strftime("%d-%m-%Y %H:%M"),
            "days": difference.days,
            "seconds": difference.seconds
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)