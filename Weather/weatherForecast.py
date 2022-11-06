from retrieveWeather import *
from map_extract import *

"""route = get_route()"""

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

testroute = [96, 138, 12, 54, 178, 54, 4195, 617, 1670, 1592, 56, 137, 349, 148, 77, 5]

def hourlySplits(route: "dict") -> dict[str, list[str]]:
    return