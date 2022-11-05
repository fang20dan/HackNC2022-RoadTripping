import requests

def get_weather(lat: str, lon: str) -> "dict[str, str]":
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation&temperature_unit=fahrenheit&precipitation_unit=inch&timezone=auto")
    response_dict: dict[str, str] = response.json()   # get the response data in JSON format
    return response_dict

def get_temp(response_dict: "dict[str, str]") -> "dict[str, str]": 
    temperatures: dict[str, str] = {}
    temperatures["time"] = response_dict["hourly"]["time"]
    temperatures["temperature"] = response_dict["hourly"]["temperature_2m"]
    return temperatures

def get_prep(response_dict: "dict[str, str]") -> "dict[str, str]": 
    temperatures: dict[str, str] = {}
    temperatures["time"] = response_dict["hourly"]["time"]
    temperatures["precipitation"] = response_dict["hourly"]["precipitation"]
    return temperatures

print(get_temp(get_weather("35.2336752", "-80.8473066")))