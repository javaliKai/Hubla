from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def home():
    return render_template("landing.html")

# I need to activate venv each time working with flask
# to activate, venv\Scripts\activate
# to deactivate, just type deactivate