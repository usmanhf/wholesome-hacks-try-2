import flask
import sql
app = flask.Flask(__name__)

@app.route("/")
def index():
    connection = sql.connect()
    hi = sql.get_entries(connection)
    print(hi)
    bye = []
    for item in hi:
        bye.append(item["text"])
    
    return flask.render_template('wholesome-webpage.html', data=bye)

@app.route('/text', methods=['POST'])
def text():
    form_text = flask.request.form['Answer']
    print(form_text)

    # check if form_text is positive!
    # if positive:
    connection = sql.connect()
    sql.add_message(form_text, connection)

    # else, show error message
    pass

    return flask.redirect("/")

if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
