from Map.map_extract import *
from carmpg_request import *
from cartank_request import *

def main():
    meters = 1609.34
    tot_range = getTankSize() * meters
    route = dict(get_route()) 

def get_dist(dict, num) -> int:

