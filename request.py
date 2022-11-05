import requests

start = "Charlotte" #input("Please enter a starting destination: ")
end =  "Raleigh" #input("Where are we Roadioing to? ")

#API call URL
url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + start + "&destination=" + end + "&key=AIzaSyAZ4JRLT7zandwa_yDpVq71vQZRD_n5z7U"

payload={}
headers = {}

#gets information from google maps API
response = requests.request("GET", url, headers=headers, data=payload)

#turns response json into dictionary
responsedict = response.json()

def extract_element_from_json(obj, path):
    '''
    Extracts an element from a nested dictionary or
    a list of nested dictionaries along a specified path.
    If the input is a dictionary, a list is returned.
    If the input is a list of dictionary, a list of lists is returned.
    obj - list or dict - input dictionary or list of dictionaries
    path - list - list of strings that form the path to the desired element
    '''
    def extract(obj, path, ind, arr):
        '''
            Extracts an element from a nested dictionary
            along a specified path and returns a list.
            obj - dict - input dictionary
            path - list - list of strings that form the JSON path
            ind - int - starting index
            arr - list - output list
        '''
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr

#getting total time/distance text and values. values are in seconds and meters respectively
distanceTotalText = extract_element_from_json(responsedict, ["routes", "legs", "distance", "text"])[0]
timeTotalText = extract_element_from_json(responsedict, ["routes", "legs", "duration", "text"])[0]
distanceTotalValue = extract_element_from_json(responsedict, ["routes", "legs", "distance", "value"])[0]
timeTotalValue = extract_element_from_json(responsedict, ["routes", "legs", "duration", "value"])[0]

#getting steps to measure time/distance for weather locations
distanceSteps = extract_element_from_json(responsedict, ["routes", "legs", "steps", "distance"])

print(distanceTotalText)
print(timeTotalText)
print(distanceTotalValue)
print(timeTotalValue)
print(distanceSteps)