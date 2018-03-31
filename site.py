from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('wholesome-webpage.html')

if __name__ == "__main__":
    app.run("localhost", port=80, debug=True)
