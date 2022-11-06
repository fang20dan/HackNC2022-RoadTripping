from map_extract import get_route
from carmpg_request import *
from find_gas_station import *

stops = []
meters = 1609.34
route = get_route()
mpg = get_mpg()
tot_range = meters * mpg * 13.2
current_tank = 0
cost = 0
current_price = find_price("Charlotte")

#Going through and figuring out what distance to stop at
def main(): 
    global current_tank
    global stops
    global meters
    global route
    global tot_range
    global current_tank
    global cost
    global current_price
    for x in range(0,len(route['distanceSteps'])):
        current_tank += route['distanceSteps'][x]['value']
        if current_tank >= tot_range:
            find_coord(x)
    add_costs()
    print(cost)
    print(stops)

#adding up the tank costs
def add_costs():
    global current_tank
    global meters
    global current_price
    global cost
    cost += ((current_tank / meters) / mpg) * current_price

#adding up the cost of a fresh tank of gas and figuring out 
def find_coord(y):
    global current_tank
    global tot_range
    global meters
    global current_price
    global cost
    global mpg
    temp_lat = 0
    temp_lng = 0
    temp_miles = current_tank - tot_range
    if temp_miles < tot_range:
        temp_rate = (current_tank - tot_range) / route['distanceSteps'][y]['value']
        cost += ((tot_range / meters) / mpg) * current_price
        temp_lat = (route['startLocationSteps'][y]['lat'] - route['endLocationSteps'][y]['lat']) * temp_rate
        temp_lng = (route['startLocationSteps'][y]['lng'] - route['endLocationSteps'][y]['lng']) * temp_rate
        addy = find_addy(str(route['startLocationSteps'][y]['lat'] + temp_lat), str(route['startLocationSteps'][y]['lng'] + temp_lng))
        stops.append(addy)
        current_price = find_price(sparse_addy(addy))
        current_tank = temp_miles
    #edge case instead distanceSteps happens to need more than 1 stop on a single direction step
    else:
        temp_rate = (current_tank - tot_range) / route['distanceSteps'][y]['value']
        cost =+ ((tot_range / meters) / get_mpg()) * current_price
        temp_lat = (route['startLocationSteps'][y]['lat'] - route['endLocationSteps'][y]['lat']) * temp_rate
        temp_lng = (route['startLocationSteps'][y]['lng'] - route['endLocationSteps'][y]['lng']) * temp_rate
        addy = find_addy(str(route['startLocationSteps'][y]['lat'] + temp_lat), str(route['startLocationSteps'][y]['lng'] + temp_lng))
        stops.append(addy)
        current_price = find_price(sparse_addy(addy))
        current_tank = temp_miles

main()