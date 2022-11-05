from extractfunction import *
from request import *


#getting total time/distance text and values. values are in seconds and meters respectively
distanceTotalText = extract_element_from_json(responsedict, ["routes", "legs", "distance", "text"])[0]
timeTotalText = extract_element_from_json(responsedict, ["routes", "legs", "duration", "text"])[0]
distanceTotalValue = extract_element_from_json(responsedict, ["routes", "legs", "distance", "value"])[0]
timeTotalValue = extract_element_from_json(responsedict, ["routes", "legs", "duration", "value"])[0]

#getting steps to measure time/distance for weather locations
distanceSteps = extract_element_from_json(responsedict, ["routes", "legs", "steps", "distance"])

print(distanceTotalText)
print(timeTotalText)
print(distanceTotalValue)
print(timeTotalValue)
print(distanceSteps)