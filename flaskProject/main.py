from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the website of Greg Pedersen"

if __name__ == "__main__":
    # Get the PORT environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
