from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dateToEpoch import insertDate
from daysNumber import daysNumber
from data_customer import data_cust
import time
import os


# driver.get('chrome://settings/clearBrowserData')
# driver = webdriver.Chrome('/Users/regy/automator/bot/chromedriver', options=chromeOptions)
data = data_cust
def cactiScrapper(selection, year, month, dateStart, dateEnd, createWholeMonth = 0):
    cid = data[selection]['cid']
    nameService = data[selection]['nameService']

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

