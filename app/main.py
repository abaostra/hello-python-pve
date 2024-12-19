from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Aman Basotra, Tanzu-PVE-Team, 1st Sample Python Based app!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
