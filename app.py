from flask import Flask
app = Flask(__name__)

@app.route("/")
def homePage():
    return "Welcome to the QA Store!"