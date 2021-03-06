# libraries
import logging
import os
import requests
import json
import sys
from flask import Flask, request
from datetime import date, timedelta

# create the flask app
app = Flask(__name__)

# variables
days_from = 3
api_token = os.getenv('API_TOKEN')
api_url_base = 'api.openweathermap.org'
# zip_code = os.getenv('ZIP_CODE')

#Handle a GET request for /
@app.route('/', methods=['GET'])
def muddy():

    #get zip_code that was passed as a parameter
    zip_code = request.args.get('zip_code')

    muddy = False
    try:
        r = requests.get(
            'https://{}/data/2.5/forecast?zip={}&appid={}&units=metric'.format(api_url_base, zip_code, api_token))

        #If the request returns ok, search 3 days from now for rain
        if r.status_code == requests.codes.ok:
            j = r.json()
            for x in j['list']:
                if x['dt_txt'].startswith(str(date.today() + timedelta(days=days_from))):
                    if 'rain' in x.keys():
                        if int(x['main']['temp_min']) > 0: #If we find rain, check the temperature
                            muddy = True
                            break

            #Print our output
            if muddy == False:
                return('NOT MUDDY')
            else:
                return('MUDDY')

        else:
            # raise('got a non-good status code')
            return('got a non-good status code')

    except Exception as e:
        # logging.debug('exception occurred {}'.format(e))
        return(e)


@app.route('/test/muddy/')
def test_muddy():
    return('MUDDY')


@app.route('/test/notmuddy/')
def test_not_muddy():
    return('NOT MUDDY')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
