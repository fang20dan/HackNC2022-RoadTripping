import requests
from extract_function import extract_element_from_json

#this is the latitutude and longitude of the certain area that we choose

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
    full_addy = sparsed_addy[1] + ", " + sparsed_addy[2][:2]
    return full_addy

#Makes the gas station call based on the city found
def find_price(city) -> float:
    url = "https://api.collectapi.com/gasPrice/fromCity?city=" + city
    header = {
        'content-type': "application/json",
        'authorization': "apikey 5BNN1dNsWIaZoSEdHY3YwR:0dg2htoc7sobrJgD68ee4S"
    }
    res = requests.request("GET", url, headers=header)
    data = res.json()
    price = extract_element_from_json(data, ["result", "state", "gasoline"])
    return float(price[0])
