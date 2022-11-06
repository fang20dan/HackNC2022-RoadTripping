import requests
import UtilsFunctions.extract_function

make = "Acura"
model = "ILX"
year = "2020"

url = 'https://api.api-ninjas.com/v1/cars?make=' + make + '&model=' + model + '&year=' + year

response = requests.request("GET", url, headers={'X-Api-Key': 'FXonr/duT4t53NEl4KetRA==sILBL3Prhi1turK4'})
responsedict = response.json()

print(extract_element_from_json(responsedict, ["combination_mpg"]))