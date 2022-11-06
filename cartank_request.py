from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

inputMake = "Acura"
inputModel = "ILX"
inputYear = "2020"

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)

driver.get('https://gastanksize.com/')

def selectCar(make, model, Year):
    makeType = driver.find_element(By.ID,'filter_make')
    makeType.send_keys(make)
    makeType.send_keys(Keys.RETURN)
    time.sleep(0.8)

    modelType = driver.find_element(By.ID,'filter_model')
    modelType.send_keys(model)
    modelType.send_keys(Keys.RETURN)
    time.sleep(0.8)

    year = driver.find_element(By.ID,'filter_model_year')
    year.send_keys(Year)
    year.send_keys(Keys.RETURN)
    time.sleep(0.8)

def getTankSize():
    first = driver.find_element(By.CLASS_NAME,'trims__item-top')
    first.click()
    tankSize = driver.find_element(By.CLASS_NAME,'trims-dropdown__title').text[11:16]
    driver.quit()
    return float(tankSize)

selectCar(inputMake, inputModel, inputYear)
print(getTankSize())



