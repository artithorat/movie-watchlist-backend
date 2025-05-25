from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Movie Watchlist Backend Running on Render!"
