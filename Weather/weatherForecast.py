from sys import get_route
 
# setting path
sys.path.append('../Map/map_extract.py')
from retrieveWeather import *

route = get_route()

weather_hourlyReport = {}

def estimateLocation(currentLocation: "dict[str, str]", nextLocation: "dict[str, str]", totalTravelTime: int, timeTillHour: int) -> "dict[str, str]":
    """returns the estimated location between two points given the time of travel"""
    estimatedLocation = {}
    scale = totalTravelTime / timeTillHour
    lat = round(((float(nextLocation["lat"]) - float(currentLocation["lat"])) / scale), 7)
    lng = round(((float(nextLocation["lng"]) - float(currentLocation["lng"])) / scale), 7)

    estimatedLocation["lat"] =  str(float(currentLocation["lat"]) + lat)
    estimatedLocation["lng"] =  str(float(currentLocation["lng"]) + lng)
    return estimatedLocation

print(estimateLocation({"lat" : "25.8", "lng" : "48.2"}, {"lat" : "-83.4", "lng" : "74.3"}, 50, 12))

route = {'distanceTotalText': '167 mi', 'timeTotalText': '2 hours 36 mins', 'distanceTotalValue': 268901, 'timeTotalValue': 9378, 'distanceSteps': [{'text': '0.2 mi', 'value': 281}, {'text': '0.5 mi', 'value': 809}, {'text': '384 ft', 'value': 117}, {'text': '0.4 mi', 'value': 588}, {'text': '2.3 mi', 'value': 3708}, {'text': '0.8 mi', 'value': 1208}, {'text': '81.0 mi', 'value': 130291}, {'text': '11.7 mi', 'value': 18890}, {'text': '32.1 mi', 'value': 51595}, {'text': '30.3 mi', 'value': 48838}, {'text': '1.0 mi', 'value': 1626}, {'text': '2.2 mi', 'value': 3598}, {'text': '3.1 mi', 'value': 4920}, {'text': '1.2 mi', 'value': 1956}, {'text': '0.3 mi', 'value': 472}, {'text': '13 ft', 'value': 4}], 'timeSteps': [96, 138, 12, 54, 178, 54, 4195, 617, 1670, 1592, 56, 137, 349, 148, 77, 5], 'startLocationSteps': [{'lat': 35.2271328, 'lng': -80.8431751}, {'lat': 35.2287765, 'lng': -80.8408224}, {'lat': 35.2336752, 'lng': -80.8473066}, {'lat': 35.2336606, 'lng': -80.8485735}, {'lat': 35.2371696, 'lng': -80.85337439999999}, {'lat': 35.2667215, 'lng': -80.8441677}, {'lat': 35.272774, 'lng': -80.8370491}, {'lat': 35.9999668, 'lng': -79.8612452}, {'lat': 36.049265, 'lng': -79.6867554}, {'lat': 36.0606489, 'lng': -79.1333262}, {'lat': 35.8207436, 'lng': -78.7441693}, {'lat': 35.81172919999999, 'lng': -78.7303702}, {'lat': 35.8034952, 'lng': -78.6930467}, {'lat': 35.7966078, 'lng': -78.6424313}, {'lat': 35.7797459, 'lng': -78.643395}, {'lat': 35.7795576, 'lng': -78.6381694}], 'endLocationSteps': [{'lat': 35.2287765, 'lng': -80.8408224}, {'lat': 35.2336752, 'lng': -80.8473066}, {'lat': 35.2336606, 'lng': -80.8485735}, {'lat': 35.2371696, 'lng': -80.85337439999999}, {'lat': 35.2667215, 'lng': -80.8441677}, {'lat': 35.272774, 'lng': -80.8370491}, {'lat': 35.9999668, 'lng': -79.8612452}, {'lat': 36.049265, 'lng': -79.6867554}, {'lat': 36.0606489, 'lng': -79.1333262}, {'lat': 35.8207436, 'lng': -78.7441693}, {'lat': 35.81172919999999, 'lng': -78.7303702}, {'lat': 35.8034952, 'lng': -78.6930467}, {'lat': 35.7966078, 'lng': -78.6424313}, {'lat': 35.7797459, 'lng': -78.643395}, {'lat': 35.7795576, 'lng': -78.6381694}, {'lat': 35.7795894, 'lng': -78.6381679}]}

print(route["timeSteps"])

def hourlySplits(route: "dict") -> dict[str, list[str]]:
    count: int = 0
    time: int = 0
    i: int = 0
    while i < len(route["timeSteps"]):
        if (count + testroute[i] < 3600):
            count += testroute[i]
            i += 1
        else:
            timeLeft: int = 3600 - count
            

        



    return