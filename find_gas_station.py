import requests
from Map.extract_function import extract_element_from_json

#google maps then goes and finds a gas station in the area
def find_addy(lat, lng) -> str:
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=gas&inputtype=textquery&locationbias=point:" + lat + ", "+ lng + "&fields=formatted_address%2Cname%2Cgeometry&key=AIzaSyAZ4JRLT7zandwa_yDpVq71vQZRD_n5z7U"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    responsedict = response.json()
    #Finds what the address of the gas station is
    return str(extract_element_from_json(responsedict, ["candidates", "formatted_address"]))

#Finds the city of the gas station
def sparse_addy(addre) -> str:
    sparsed_addy = addre.split(", ")
    return sparsed_addy[1]

#Makes the gas station call based on the city found
def find_price(city) -> float:
    url = "https://api.collectapi.com/gasPrice/fromCity?city=" + city
    header = {
        'content-type': "application/json",
        'authorization': "apikey 61KmAIy0Wnoqzyd3I5LK42:5cyO5xkMbDuM2yxHJGxuG0"
    }
    res = requests.request("GET", url, headers=header)
    data = res.json()
    price = extract_element_from_json(data, ["result", "state", "gasoline"])
    return price[0]
