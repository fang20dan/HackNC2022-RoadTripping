from Map.extract_function import *
from Map.map_extract import get_route
from carmpg_request import *
from cartank_request import *

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

def find_coord(y):
    temp_lat = 0
    temp_lng = 0
    temp_miles = current_tank - tot_range
    temp_rate = (current_tank - tot_range) / tot_range
    cost =+ ((tot_range / meters) / get_mpg()) * current_price

    

main()