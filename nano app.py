from flask import Flask, render_template

app = Flask(__name__)

patients=[
"Aarav Sharma",
"Diya Patel",
"Rohan Verma",
"Ananya Reddy",
"Vikram Singh",
"Meera Nair",
"Rahul Das",
"Kavya Iyer",
"Arjun Mehta",
"Sneha Kulkarni"
]

@app.route("/")
def home():
    return render_template("index.html",patients=patients)

app.run(host="0.0.0.0",port=5000)
