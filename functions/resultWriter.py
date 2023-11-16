from datetime import datetime
import json

# function to write results out to a named json thats constructed from city and the time the program was run
def writeResultsToFile(city:str,temperatureResults):
    print("Writing to file...")
    FILENAME = city.lower() + "_" + datetime.now().strftime("%Y_%m_%d_T%H:%M:%SZ") + ".json"
    file = open("./outputs/" + FILENAME,"w")
    json.dump(temperatureResults,file)
    print("Finished writing to file -",FILENAME)




