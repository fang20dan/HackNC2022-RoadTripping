import requests
from Map.extract_function import *

make = "Acura"
model = "ILX"
year = "2020"
def get_mpg() -> int:
    url = 'https://api.api-ninjas.com/v1/cars?make=' + make + '&model=' + model + '&year=' + year

    response = requests.request("GET", url, headers={'X-Api-Key': 'FXonr/duT4t53NEl4KetRA==sILBL3Prhi1turK4'})
    responsedict = response.json()

    return extract_element_from_json(responsedict, ["combination_mpg"])[0][0]