from extract_function import *
from map_request import *


def get_route():
    route = {}
    #getting total time/distance text and values. values are in seconds and meters respectively
    route["distanceTotalText"] = extract_element_from_json(responsedict, ["routes", "legs", "distance", "text"])[0]
    route["timeTotalText"] = extract_element_from_json(responsedict, ["routes", "legs", "duration", "text"])[0]
    route["distanceTotalValue"] = extract_element_from_json(responsedict, ["routes", "legs", "distance", "value"])[0]
    route["timeTotalValue"] = extract_element_from_json(responsedict, ["routes", "legs", "duration", "value"])[0]

    #getting steps to measure time/distance/locations for weather measurements
    route["distanceSteps"] = extract_element_from_json(responsedict, ["routes", "legs", "steps", "distance"])
    route["timeSteps"] = extract_element_from_json(responsedict, ["routes", "legs", "steps", "duration", "value"])
    route["startLocationSteps"] = extract_element_from_json(responsedict, ["routes", "legs", "steps", "start_location"])
    route["endLocationSteps"] = extract_element_from_json(responsedict, ["routes", "legs", "steps", "end_location"])
    return route

def get_totalDistance():
    return str(get_route()["distanceTotalText"])

print(get_totalDistance())