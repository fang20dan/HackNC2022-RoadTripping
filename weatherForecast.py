from map_extract import get_route
from retrieveWeather import get_weather
from datetime import datetime, timedelta

lat = "35.899963968159"
lng = "-79.04617075972824"

route = get_route()
weather_hourlyReport = {}
weather = get_weather(lat, lng)

def estimateLocation(currentLocation: "dict[str, str]", nextLocation: "dict[str, str]", totalTravelTime: int, scale: float) -> "dict[str, str]":
    """Helper function that returns the estimated location between two points given the time of travel"""
    estimatedLocation = {}
    lat = round(((float(nextLocation["lat"]) - float(currentLocation["lat"])) / scale), 7)
    lng = round(((float(nextLocation["lng"]) - float(currentLocation["lng"])) / scale), 7)

    estimatedLocation["lat"] =  str(float(currentLocation["lat"]) + lat)
    estimatedLocation["lng"] =  str(float(currentLocation["lng"]) + lng)
    return estimatedLocation

def splitLocations(route: "dict") -> "list":
    """Function that finds the coordinates of each hour along the route"""
    count: int = 0
    i: int = 0
    locationSplits: list[dict] = []
    while i < len(route["timeSteps"]):
        if (count + route["timeSteps"][i] < 3600):
            count += route["timeSteps"][i]
        else:
            timeLeft: int = 3600 - count
            scale = round((route["timeSteps"][i] / timeLeft), 7)
            locationSplits.append(estimateLocation(route["startLocationSteps"][i], route["endLocationSteps"][i], route["timeSteps"], scale))
            count = route["timeSteps"][i] - timeLeft
        i += 1
    if (count > 900):
        locationSplits.append(route["endLocationSteps"][len(route["timeSteps"])-1])
    return locationSplits

def splitTimes(splits: int) -> "list":
    """Helper function that finds the time of each hour split"""
    result: list[str] = []
    i: int = 1
    while i <= splits:
        nextsplit = datetime.now() + timedelta(hours=i)
        time: str = format(nextsplit, '%Y-%m-%dT')
        if (int(nextsplit.strftime("%M")) <= 30):
            time += nextsplit.strftime("%H") + ":00"
        else:
            nnsplit = nextsplit + timedelta(hours=1)
            time += nnsplit.strftime("%H") + ":00"
        result.append(time)
        i += 1
    return result


def reportHourlyWeather(route: "dict", locations: "list") -> "dict":
    """Generates the hourly weather report"""
    weather_hourlyReport: dict = {}
    times = splitTimes(len(locations))
    i: int = 0
    while i < len(locations):
        j: int = 0
        while j < len(route['time']):
            if (route['time'][j] == times[i]):
                splitinfo: list = []
                splitinfo.append(route["temperature"][j])
                splitinfo.append(route["precipitation"][j])
                weather_hourlyReport[times[i]] = splitinfo
            j += 1
        i += 1
    return weather_hourlyReport

weather_hourlyReport = reportHourlyWeather(weather, splitLocations(route))