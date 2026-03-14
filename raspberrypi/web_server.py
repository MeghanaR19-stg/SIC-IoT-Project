from flask import Flask,render_template,request

app=Flask(__name__)

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

@app.route("/",methods=["GET","POST"])
def home():

    data=None
    alert=False

    if request.method=="POST":

        name=request.form["patient"]

        with open("healthdata.txt") as f:
            lines=f.readlines()

        for line in reversed(lines):

            if name in line:

                parts=line.split()

                heart=int(parts[-2])
                temp=float(parts[-1])

                data={"name":name,"heart":heart,"temp":temp}

                if heart>120:
                    alert=True

                break

    return render_template("index.html",patients=patients,data=data,alert=alert)

app.run(host="0.0.0.0",port=5000)
