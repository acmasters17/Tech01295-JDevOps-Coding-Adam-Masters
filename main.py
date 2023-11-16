from functions.weatherRequester import makeWeatherRequestFor
from functions.weatherParser import parseWeatherForMinMaxTemps


resultingData = makeWeatherRequestFor("London")

if(resultingData != None):
    # Know we have data so now parse 
    parsedResult = parseWeatherForMinMaxTemps(resultingData)
else:
    # Know something has gone wrong so halt execution for this cycle
    print("Something went wrong")






print("Hello world")


