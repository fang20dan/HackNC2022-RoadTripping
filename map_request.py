import requests

start = "Chapel Hill" #input("Please enter a starting destination: ")
end =  "San Diego" #input("Where are we Roadioing to? ")

#API call URL
url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + start + "&destination=" + end + "&key=AIzaSyAZ4JRLT7zandwa_yDpVq71vQZRD_n5z7U"

payload = {}
headers = {}

#gets information from google maps API and stores as json
response = requests.request("GET", url, headers=headers, data=payload)

#turns response json into dictionary
responsedict = response.json()

