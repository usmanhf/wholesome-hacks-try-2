import flask
import requests
#import azure.cognitiveservices.language.textanalytics as textanalytics
#from azure.cognitiveservices.language.textanalytics.models.multi_language_input import MultiLanguageInput
#from azure.common.credentials import ServicePrincipalCredentials
import sql

app = flask.Flask(__name__)

@app.route("/")
def index():
    connection = sql.connect()
    all_responses = sql.get_entries(connection)
    bye = []
    for item in all_responses:
        bye.append(item["text"])
    
    return flask.render_template('wholesome-webpage.html', data=bye)

@app.route('/text', methods=['POST'])
def text():
    form_text = flask.request.form['Answer']
    print(form_text)

    # check if form_text is positive!
    # credentials = ServicePrincipalCredentials(
    #     client_id="",
    #     tenant="",
    #     secret="")
    # textanalyticsapi = textanalytics.text_analytics_api.TextAnalyticsAPI("westus2", credentials)
    # document = MultiLanguageInput(language="en", id="0", text=form_text)
    # sentiment_number = textanalyticsapi.sentiment(documents=[document])
    # print(sentiment_number)

    documents = {'documents': [
        {'id': '1', 'text': form_text, 'language': 'en'}
    ]}
    headers   = {"Ocp-Apim-Subscription-Key": ""}
    response  = requests.post("https://westus2.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment",
                              headers=headers,
                              json=documents)
    sentiments = response.json()
    print(sentiments['documents'][0]['score'])

    if sentiments['documents'][0]['score'] >= 0.67: # if positive message
        connection = sql.connect()
        sql.add_message(form_text, connection)

    else:
        return "Positive messages only, please!"

    return flask.redirect("/")

if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
