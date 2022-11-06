from Map.map_extract import get_route
from carmpg_request import *
from cartank_request import *
from find_gas_station import *

stops = []
meters = 1609.34
route = get_route()
tot_range = getTankSize() * meters * get_mpg()
current_tank = 0
cost = 0
current_price = 2.03

#Going through and figuring out what distance to stop at
def main():   
    for x in route['distanceSteps']:
        current_tank =+ route['distanceSteps'][x]['value']
        if current_tank >= tot_range:
            find_coord(x)
    add_costs()
            

#adding up the tank costs
def add_costs():
    cost =+ ((current_tank / meters) / get_mpg()) * current_price

#adding up the cost of a fresh tank of gas and figuring out 
def find_coord(y):
    temp_lat = 0
    temp_lng = 0
    temp_miles = current_tank - tot_range
    if temp_miles < tot_range:
        temp_rate = (current_tank - tot_range) / route['distanceSteps'][y]['value']
        cost =+ ((tot_range / meters) / get_mpg()) * current_price
        temp_lat = (route['startLocationSteps'][y]['lat'] - route['endLocationSteps'][y]['lat']) * temp_rate
        temp_lng = (route['startLocationSteps'][y]['lng'] - route['endLocationSteps'][y]['lng']) * temp_rate
        addy = find_addy(route['startLocationSteps'][y]['lat'] + temp_lat, route['startLocationSteps'][y]['lng'] + temp_lng)
        stops.append(addy)
        current_price = find_price(sparse_addy(addy))
        current_tank = temp_miles
    #edge case instead distanceSteps happens to need more than 1 stop on a single direction step
    else:
        temp_rate = (current_tank - tot_range) / route['distanceSteps'][y]['value']
        cost =+ ((tot_range / meters) / get_mpg()) * current_price
        temp_lat = (route['startLocationSteps'][y]['lat'] - route['endLocationSteps'][y]['lat']) * temp_rate
        temp_lng = (route['startLocationSteps'][y]['lng'] - route['endLocationSteps'][y]['lng']) * temp_rate
        addy = find_addy(route['startLocationSteps'][y]['lat'] + temp_lat, route['startLocationSteps'][y]['lng'] + temp_lng)
        stops.append(addy)
        current_price = find_price(sparse_addy(addy))
        current_tank = temp_miles
        find_coord(y)

main()