from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
import requests 
import pandas as pd
import json
# chrome_binary = 'binaries/Google Chrome for Testing 119.app/Contents/MacOS/Google Chrome for Testing'
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# options.binary_location = chrome_binary
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

def verify_title():
    # driver.get("https://access.clarivate.com/login?app=cortellis&status=nosso")
    # url = 'https://www.cortellis.com/intelligence/search/allresults?entityType=nextgendrugall&viewAllLinkIdentifier=drugLink'
    # driver.get(url)
    title = driver.title
    
    excepted_title = "Google"
    if title == excepted_title:
        print("Test Passed")
    else:
        print("Test Failed")
        print(title)
    
def selectDrug():
    driver.find_element("xpath", '//*[@id="formfieldNumberResults"]/option[5]').click()
    time.sleep(2)
    driver.find_element("xpath", '//*[@id="resultsTableFixed"]/thead/tr/th[1]/label').click()

    for i in range(1, 101):
        xpath = '//*[@id="resultsTableFixed"]/tbody/tr[ ' + str(i) + ' ]/td[1]/label'
        element = driver.find_element("xpath", xpath)
        actions = ActionChains(driver)
        # actions.scroll_to_element(element)
        actions.move_to_element(element).perform()
        driver.execute_script("arguments[0].click();", element)    

def getdata():
    # xpath = '//*[@id="gt-content-inner-cortellis"]/div[2]/div/div/div[1]/span[3]/span[2]/a'
    # # element = driver.find_element("xpath", xpath)
    # driver.find_element("xpath", xpath).click()  
    # time.sleep(2)
    # xpath = '/html/body/div[11]/div[2]/success-predictor/div/div[1]/div[2]/div[1]'
    # driver.find_element("xpath", xpath).click()
    # time.sleep(2)
    # xpath = '/html/body/div[11]/div[2]/success-predictor/div/div[1]/div[1]/div[2]/div[1]/div[2]'
    # driver.find_element("xpath", xpath).click()
    response = requests.get('https://www.cortellis.com/intelligence/predictor/predictions.do')
    if response.status_code == 200:
        print("Success")
        print(response.text)
        # json_data = response.json()
        # print(json_data)
    else:   
        print("Error")

def readData():
    with open('/Users/zonglianghan/Desktop/drug/data3.json') as f:
        d = json.load(f)
    
    df = pd.json_normalize(d, record_path=['drugSuccessPredictions'])
    # df = df.drop(columns=[''])
    df_prog = pd.json_normalize(data=d['drugSuccessPredictions'], record_path='drugPrograms', meta=['drugId', 'displayName'], max_level=2)
    df_prog.to_csv('data.csv')
    print(df_prog.head())
if __name__ == '__main__':
    # verify_title()
    # selectDrug()
    # getdata()
    readData()
    # while True:
    #     pass