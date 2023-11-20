from env import weatherAPIKey
import requests

# api-endpoint
URL = "https://durvp011gk.execute-api.eu-west-1.amazonaws.com/v1/api/forecasts"
 

def makeWeatherRequestFor(city):
    print("Making weather request for " + city + "...")
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'city': city}
 
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS, headers={'x-api-key': weatherAPIKey})

    if(r.ok):
        print("Successful weather request made!")
        return r.json()
    elif(r.status_code == 403):
        print("Request Forbidden - please ensure you have registered your api key by following the read me and creating an env.py file")
    else:
        print("Sorry something went wrong - ",r.status_code)
