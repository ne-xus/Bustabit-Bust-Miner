import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

import pandas as pd
# path to the firefox binary inside the Tor package
binary = '/Applications/Tor Browser 2.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)

browser = webdriver.Firefox(firefox_binary = firefox_binary)

import time

# time.sleep(60)

browser.get('https://www.bustabit.com')
button = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/a')
button.click()
# time.sleep(30)

busts = []
dates = []
from datetime import datetime
time.sleep(5)
previous_bust = 0
while True:
    value = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[1]/div[1]/div[1]/div/div[3]/table/tbody/tr/td[1]/a')
    value = value.text
    if previous_bust != value:
        print(value)
        previous_bust = value
        date = datetime.now()
        busts.append(value)
        dates.append(date)
        bust = pd.DataFrame({'bust_point': busts,
                              'dates': dates})
        bust.to_csv('bust_data.csv')

time.sleep(600)
browser.quit()
