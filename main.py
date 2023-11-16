from functions.weatherRequester import makeWeatherRequestFor
from functions.weatherParser import parseWeatherForMinMaxTemps
from functions.resultWriter import writeResultsToFile


resultingData = makeWeatherRequestFor("London")

if(resultingData != None):
    # Know we have data so now parse 
    parsedResult = parseWeatherForMinMaxTemps(resultingData)

    if(parsedResult != None):
        writeResultsToFile("London", parsedResult)
    else:
        print("Something went wrong")
        
else:
    # Know something has gone wrong so halt execution for this cycle
    print("Something went wrong")






print("Hello world")


