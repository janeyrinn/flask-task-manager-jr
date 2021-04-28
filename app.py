import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
# Renders bson format from Pymongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


# Creates an instance of the flask app
app = Flask(__name__)

# App configuration with database
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# Instance of PyMongo and add the app into in
mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    # will generate date from our tasks collection
    tasks = mongo.db.tasks.find()
    return render_template("tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
