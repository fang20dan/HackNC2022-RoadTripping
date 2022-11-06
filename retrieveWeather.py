import requests

def get_weather(lat: str, lon: str) -> "dict[str, str]":
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation&temperature_unit=fahrenheit&precipitation_unit=inch&timezone=auto")
    response_dict: dict[str, str] = response.json()   # get the response data in JSON format
    weather: dict[str, str] = {}
    weather["time"] = response_dict["hourly"]["time"]
    weather["temperature"] = response_dict["hourly"]["temperature_2m"]
    weather["precipitation"] = response_dict["hourly"]["precipitation"]
    return weather