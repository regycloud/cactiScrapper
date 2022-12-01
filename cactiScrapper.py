from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dateToEpoch import insertDate
from daysNumber import daysNumber
import time
import os


# driver.get('chrome://settings/clearBrowserData')
# driver = webdriver.Chrome('/Users/regy/automator/bot/chromedriver', options=chromeOptions)
data = {
    '1' : {
        'cid' : 8254,
    }
}

def cactiScrapper(selection, year, month, dateStart, dateEnd, createWholeMonth = 0):
    if selection == 1 :
        cid = 8254
    if selection == 2 :
        cid = 10022
    if selection == 3 :
        cid = 11301
    if selection == 4 :
        cid = 11356
    if selection == 5 :
        cid = 10690
    if selection == 6 :
        cid = 11213
    if selection == 7: 
        cid = 11211
    if selection == 8: 
        cid = 11357
    if selection == 9: 
        cid = 7424
    if selection == 10: 
        cid = 8381 
    if selection == 11:
        cid = 11869
    if selection == 12:
        cid = 11872
    if selection == 13:
        cid = 10046
    if selection == 14:
        cid = 9502
    if selection == 15:
        cid = 11953

    # Define the name by cid:
    if cid == 8254: #1
        nameService = 'PGAS.VAL.33.01#1'
    if cid == 10022: #2
        nameService = 'PGAS.VAL.33.01#2'
    if cid == 11301: #3
        nameService = 'PGAS.VAL.33.04' # HE#2
    if cid == 11356: #4
        nameService = 'PGAS.VAL.43.01'
    if cid == 10690: #5
        nameService = 'PGAS.VAL.43.02'
    if cid == 11213: #6
        nameService = 'PGAS.VAL.43.03'
    if cid == 11211: #7
        nameService = 'PGAS.VAL.43.04'
    if cid == 11357: #8
        nameService = 'PGAS.VAL.43.05'
    if cid == 7424: #9
        nameService = 'NTT'
    if cid == 8381: #10
        nameService = 'TELIA'
    if cid == 11869: #11
        nameService = 'PGAS.VAL.33.05' # HE#3
    if cid == 11872: #12
        nameService = 'PGAS.VAL.33.06' # HE#4
    if cid == 10046: #13
        nameService = 'PCCW'
    if cid == 9502: #14
        nameService = 'TATA'
    if cid == 11953: #15
        nameService = 'PGAS.VAL.43.06'

    print('Your selection is {selection}, for year {year}/{month} from {dateStart} to {dateEnd}'.format(selection = nameService, year = year, month = month, dateStart = dateStart, dateEnd = dateEnd))
    confirm = input('continue? ')
    if confirm == 'n':
        exit()

    os.environ['WDM_LOG'] = '0'
    chromeOptions = Options()
    # chromeOptions.add_experimental_option("debuggerAddress", "localhost:9222")
    chromeOptions.add_argument('--headless')
    driver = webdriver.Chrome('./chromedriver', options=chromeOptions)

    # Access MRTG site
    driver.get("http://customer.pgascom.co.id/cacti/")

    # login
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user_row"]/td[2]/input'))).send_keys("pgasint")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password_row"]/td[2]/input'))).send_keys("pgasint1234")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/tbody/tr[8]/td/input'))).click()

    # do the repetition
    while dateStart <= dateEnd:

        # convert date to epoch
        start = insertDate(year,month,dateStart)[0]
        end = insertDate(year,month,dateStart)[1]

        # search CID graph
        driver.get("http://customer.pgascom.co.id/cacti/graph.php?action=zoom&local_graph_id={cid}&rra_id=0&graph_start={start}&graph_end={end}".format(start = start, end=end, cid = cid))

        # Download graph image
        with open('{nameService} - {date}.png'.format(nameService = nameService, date = dateStart), 'wb') as file:
            img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="zoomGraphImage"]')))
            time.sleep(1)
            file.write(img.screenshot_as_png)
        
        print('{nameService} date of {date} is completed.'.format(nameService = nameService, date=dateStart))

        # do the increment
        dateStart += 1

    # Scrap a graph from the first until end of month
    start = insertDate(year,month,1)[0]
    end = insertDate(year,month,30)[1]

    if createWholeMonth == 1:
        end = insertDate(year,month,daysNumber(year, month))[1]
        driver.get("http://customer.pgascom.co.id/cacti/graph.php?action=zoom&local_graph_id={cid}&rra_id=0&graph_start={start}&graph_end={end}".format(start = start, end=end, cid = cid))

        with open('{nameService} - {date}.png'.format(nameService = nameService, date = 32), 'wb') as file:
            img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="zoomGraphImage"]')))
            time.sleep(1)
            file.write(img.screenshot_as_png)
            print('{nameService} date of {date} is completed.'.format(nameService = nameService, date = dateEnd + 1))


# NTT
# cactiScrapper(9, 2022, 9, 1, daysNumber(2022, 9), 1)

# # PCCW
# cactiScrapper(13, 2022, 10, 1, daysNumber(2022, 10), 1)

# # TATA
# cactiScrapper(14, 2022, 10, 1, daysNumber(2022, 10), 1)

# PGAS.VAL.43.06
# cactiScrapper(15, 2022, 8, 1, daysNumber(2022, 8), 1)
# cactiScrapper(15, 2022, 9, 1, daysNumber(2022, 9), 1)



# TELIA
# cactiScrapper(8381, 2022, 8, 1, 31, 1)
# cactiScrapper(11356, 2022, 7, 1, 31, 1)
# cactiScrapper(10690, 2022, 7, 1, 31, 1)

# HE#2
# cactiScrapper(3, 2022, 10,  1, daysNumber(2022, 10), 1)
# HE#3
# cactiScrapper(11, 2022, 10, 1, daysNumber(2022, 10), 1)
# HE#4
# cactiScrapper(12, 2022, 10, 1, daysNumber(2022, 10), 1)


# cactiScrapper(11213, 2022, 7, 1, 31, 1)

# cactiScrapper(11211, 2022, 7, 1, 31, 1)

# cactiScrapper(11357, 2022, 7, 1, 31, 1)

