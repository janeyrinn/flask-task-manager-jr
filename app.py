import os
from flask import Flask
if os.path.exists("env.py"):
    import env 

# Creates an instance of flask stored in a variable called "app"
app = Flask(__name__)

# Test function to check app is properly configured
@app.route("/")
def hello():
    return "Hello World ... again!"

# Tells how and where to run our app 
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)