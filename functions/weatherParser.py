from datetime import datetime

# Function is going to take in a valid weather json and proceed to parse it for the min and max day in each dataset
def parseWeatherForMinMaxTemps(weatherData):
    print("Parsing returned weatherdata...")

    # try:
    locationProperties = weatherData['features'][0]['properties']

    dateDictionary = {}

    # if we get location properties iterate through the returned times and for each one compare the screenTemperature
    for xTime in locationProperties["timeSeries"]:
            screenTempAtTime = float(xTime["screenTemperature"])
            timeStamp = datetime.strptime(xTime["time"],"%Y-%m-%dT%H:%MZ")

            keyTimeStamp = str(timeStamp.date())
            print(keyTimeStamp)

            if keyTimeStamp in dateDictionary:
                 currentHighTemp = float(dateDictionary[keyTimeStamp]["maxTemperature"])
                 currentLowTemp = float(dateDictionary[keyTimeStamp]["minTemperature"])
                 print(currentHighTemp, currentLowTemp)
                 # update our dictionary key with new temps if they exceed values
                 dateDictionary[keyTimeStamp]["maxTemperature"] = screenTempAtTime if screenTempAtTime > currentHighTemp else currentHighTemp
                 dateDictionary[keyTimeStamp]["minTemperature"] = screenTempAtTime if screenTempAtTime < currentLowTemp else currentLowTemp
            else:
                 print("Creating new key")
                 # first temp for day so create our key value pair with first temps
                 dateDictionary[keyTimeStamp] = {"maxTemperature": screenTempAtTime, "minTemperature": screenTempAtTime}

        # here we have now gone through all the times so now know highest and lowest for
    print(dateDictionary)

    # except:
    #     print("Error parsing response back, please try again later!")


    print("Data successfully parsed")


