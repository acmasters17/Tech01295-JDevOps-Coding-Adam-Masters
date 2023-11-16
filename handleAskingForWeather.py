from functions.weatherRequester import makeWeatherRequestFor
from functions.weatherParser import parseWeatherForMinMaxTemps
from functions.resultWriter import writeResultsToFile

# main event loop for asking for the asking for weather flow
def handleAskingForWeather():
    print("\nYou have selected to use the weather querier!\n")

    city = None
    while city == None:
        try:
            city = str(input("Please enter a city you would like to find the miminum and maximum temperatures for: "))
            if(len(city) == 0):
                print("Sorry please enter a city that has one or more characters!")
                city = None
            else:
                # Now have a city so begin exectution path to file generation
                resultingData = makeWeatherRequestFor(city)
                if(resultingData == None):
                    print("Sorry the data could not be fetched, please try again later!")
                else:
                    # got request data so parse
                    parsedResult = parseWeatherForMinMaxTemps(resultingData)
                    if(parsedResult == None):
                        print("Sorry the data received could not be parsed, please try again later!")
                    else:
                        # data is parsed and ready so write to file
                        writeResultsToFile(city,parsedResult)
                        # print success message
                        print("Thanks for using the weather querier!")
        except:
            print("Please only enter a city name!")
            city = None
