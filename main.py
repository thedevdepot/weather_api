from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def home(station, date):
    df.pd.read_csv("")
    temperatrue = df.station(date)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5042)