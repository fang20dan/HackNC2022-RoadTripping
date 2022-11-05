from extractFunction import *
from map_request import *


#getting total time/distance text and values. values are in seconds and meters respectively
distanceTotalText = extract_element_from_json(responsedict, ["routes", "legs", "distance", "text"])[0]
timeTotalText = extract_element_from_json(responsedict, ["routes", "legs", "duration", "text"])[0]
distanceTotalValue = extract_element_from_json(responsedict, ["routes", "legs", "distance", "value"])[0]
timeTotalValue = extract_element_from_json(responsedict, ["routes", "legs", "duration", "value"])[0]

#getting steps to measure time/distance/locations for weather measurements
distanceSteps = extract_element_from_json(responsedict, ["routes", "legs", "steps", "distance"])
timeSteps = extract_element_from_json(responsedict, ["routes", "legs", "steps", "duration"])
startLocationSteps = extract_element_from_json(responsedict, ["routes", "legs", "steps", "start_location"])
endLocationSteps = extract_element_from_json(responsedict, ["routes", "legs", "steps", "end_location"])

print(distanceTotalText)
print(timeTotalText)
print(distanceTotalValue)
print(timeTotalValue)
print(distanceSteps)
print(timeSteps)
print(startLocationSteps)
print(endLocationSteps)