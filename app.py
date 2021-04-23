from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def home():
    return render_template("landing.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    # Handling get request
    if request.method == "GET":
        return render_template("register.html")
    
    # Handling post request
    if request.method == "POST":
        return "<h1>NOT FOUND</h1>"
        # TODO:
        # 1. add re-type password logic
        # 2. handle form to sql
        # 3. alert register sucess using bootstrap

@app.route('/login', methods=["GET", "POST"])
def login():
    # Handling get request
    if request.method == "GET":
        return render_template("login.html")
    
    # Handling post request
    if request.method == "POST":
        return "<h1>NOT FOUND</h1>"
        # TODO:
        # 1. query from sql, and check
        # 2. add username to session