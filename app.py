from requests import Request, Session, Response
import os

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    lat = request.args["lat"]
    long = request.args["lon"]
    apiKey = os.environ['API_KEY']
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'lat': lat,
            'lon': long,
            'appid': apiKey
        }
        session = Session()
        request = Request('GET', url, params=params)
        prepped = request.prepare()
        response = session.send(prepped)
        return response.json()
    
    except Exception as e:
        return e

app.run(port=8081)