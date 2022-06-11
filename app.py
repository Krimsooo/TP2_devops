import flask
from requests import Request, Session, Response
import os

from flask import request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    lat = request.args["lat"]
    long = request.args["lon"]
    apiKey = os.environ['API_KEY']

    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': lat,
        'lon': long,
        'appid': apiKey
    }
    session = Session()
    requete = Request('GET', url, params=params)
    prepped = requete.prepare()
    response = session.send(prepped)
    return response.json()

app.run(port=8081)
