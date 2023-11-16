from datetime import datetime

# Function is going to take in a valid weather json and proceed to parse it for the min and max day in each dataset
def parseWeatherForMinMaxTemps(weatherData):
    print("Parsing returned weatherdata...")

    try:
        # get part of response data we actually want to use
        locationProperties = weatherData['features'][0]['properties']

        # initalise a date dictionary for our return object
        dateDictionary = {}

        # if we get location properties iterate through the returned times and dates and cumulatively build our dictionary
        for xTime in locationProperties["timeSeries"]:
            # getting the temperature and timestamp for each time
            screenTempAtTime = float(xTime["screenTemperature"])
            timeStamp = datetime.strptime(xTime["time"],"%Y-%m-%dT%H:%MZ")

            # taking just date part for dictionary key so we compare for each day
            keyTimeStamp = str(timeStamp.date())

            if keyTimeStamp in dateDictionary:
                 # not the first temperature for the day so compare with existing
                 currentHighTemp = float(dateDictionary[keyTimeStamp]["maxTemperature"])
                 currentLowTemp = float(dateDictionary[keyTimeStamp]["minTemperature"])
                 # update our dictionary key with new temps if they exceed values
                 dateDictionary[keyTimeStamp]["maxTemperature"] = screenTempAtTime if screenTempAtTime > currentHighTemp else currentHighTemp
                 dateDictionary[keyTimeStamp]["minTemperature"] = screenTempAtTime if screenTempAtTime < currentLowTemp else currentLowTemp
            else:
                 # first temp for the day so create our key value pair with first temps
                 dateDictionary[keyTimeStamp] = {"maxTemperature": screenTempAtTime, "minTemperature": screenTempAtTime}

        # here we have now gone through all the times so now know highest and lowest for a date range so return our dictionary
        print("Data successfully parsed")
        return dateDictionary

    except:
        print("Error parsing response data, please try again later!")


