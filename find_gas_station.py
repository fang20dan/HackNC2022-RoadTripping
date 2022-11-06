import requests
from UtilsFunctions.extract_function import extract_element_from_json

#this is the latitutude and longitude of the certain area that we choose
lat = str(35.2271)
lng = str(-80.8431)

#google maps then goes and finds a gas station in the area
url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=gas&inputtype=textquery&locationbias=point:" + lat + ", "+ lng + "&fields=formatted_address%2Cname%2Cgeometry&key=AIzaSyAZ4JRLT7zandwa_yDpVq71vQZRD_n5z7U"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
responsedict = response.json()

#Finds what the address of the gas station is
address = str(extract_element_from_json(responsedict, ["candidates", "formatted_address"]))

#Finds the city of the gas station
sparsed_addy = address.split(", ")
city = sparsed_addy[1]

#Makes the gas station call based on the city found
url = "https://api.collectapi.com/gasPrice/fromCity?city=" + city
header = {
    'content-type': "application/json",
    'authorization': "apikey 61KmAIy0Wnoqzyd3I5LK42:5cyO5xkMbDuM2yxHJGxuG0"
    }
res = requests.request("GET", url, headers=header)
data = res.json()

price = extract_element_from_json(data, ["result", "state", "gasoline"])
price = price[0]
print(float(price))