from Map.extract_function import *
from Map.map_extract import get_route
from carmpg_request import *
from cartank_request import *

def main():
    meters = 1609.34
    #tot_range = getTankSize() * meters
    #current_tank = tot_range
    stops = []
    route = get_route()
    print(route['distanceSteps'][2]['value'])

main()