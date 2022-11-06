from Map.extract_function import *
from Map.map_extract import get_route
from carmpg_request import *
from cartank_request import *

stops = []
meters = 1609.34
route = get_route()
#tot_range = getTankSize() * meters
current_tank = 0


def main():   
    for x in route['distanceSteps']:
        current_tank += route['distanceSteps'][x]['value']

main()