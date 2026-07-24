from flask import Flask, render_template
import redis

app = Flask(__name__)
# r = redis.Redis(host='redis', port=6379)

students = [
    {"name": "Aman", "class": "10th", "marks": 88},
    {"name": "Riya", "class": "10th", "marks": 92},
    {"name": "Karan", "class": "9th", "marks": 75}
]

# @app.route("/")
# def home():
#     return "server is running successfully"

@app.route("/")
def home():
    # visits = r.incr("visits")
    return render_template("index.html", students=students)

app.run(host="0.0.0.0", port=5000, debug=True)
