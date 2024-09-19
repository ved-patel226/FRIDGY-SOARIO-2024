from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.github import make_github_blueprint, github

from py_tools import *

app = Flask(__name__)
app.secret_key = env_to_var("APP_SECRET")

github_blueprint = make_github_blueprint(client_id=env_to_var("GITHUB_CLIENT_ID"),
                                         client_secret=env_to_var("GITHUB_CLIENT_SECRET"))

app.register_blueprint(github_blueprint, url_prefix="/login")


@app.route('/')
def index():
    if not github.authorized:
        return render_template("index.html")
    
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)