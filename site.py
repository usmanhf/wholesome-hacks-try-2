from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('wholesome-webpage.html')

@app.route('/text', methods=['POST'])
def text():
    projectpath = request.form['projectFilepath']
    # your code
    # return a response

if __name__ == "__main__":
    app.run("localhost", port=80, debug=True)
