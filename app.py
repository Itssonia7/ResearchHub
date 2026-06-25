from flask import (Flask,render_template,request,redirect,url_for)
app=Flask(__name__)

@app.route("/")
def home():
    name="Sonia"
    return render_template("home.html",name=name)

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":

        name=request.form["name"]
        email=request.form["email"]

        print(name)
        print(email)

        return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        print(email)

        return redirect(url_for("home"))
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)