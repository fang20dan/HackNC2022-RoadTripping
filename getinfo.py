from map_extract import *
from weatherForecast import *
from find_gas_station import *
from gas_stops import *

print("Starting Location: " + get_route()["startingLocation"])
print("End Location: " + get_route()["endingLocation"])
print("Total Distance: " + get_route()["distanceTotalText"])
print("Total Time: " + get_route()["timeTotalText"])
print("Weather Throughout Trip (Temp, Precip): " + str(reportHourlyWeather(get_weather("35.899963968159", "-79.04617075972824"), splitLocations(get_route()))))
print("Gas Total Cost Throughout Trip: " + str(returnCost()))
print("Stops to Make for Gas: " + str(returnStops()))