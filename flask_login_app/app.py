from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "password":
        return "Login successful!"
    else:
        return "Invalid credentials!", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
