#################################################
###    1. GET THE NAMES OF THE COUNTRIES      ###
###             FROM THE WEBSITE              ###
#################################################

# The result of this codes does not exceed 100 pages
# Therefore a boolean parameter to stop the scrapping
# is not set.

# Author of Code: Lashari Gochiashvili
# Load main packages and libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver settings
gecko_path = 'C:/Users/Lasha/anaconda3/geckodriver.exe'

options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, executable_path = gecko_path)

url = 'https://openaq.org/#/countries?_k=gv4bjc'
driver.get(url)
wait = WebDriverWait(driver, 5)
driver.implicitly_wait(5)

# Scrapping country names (e.g. Afghanistan, Austria, etc) using class name
# We will need country names to generate links to each country page
# We will generate links at the second stage.
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card__title')))
countries = driver.find_elements_by_class_name('card__title')

# This function creates a list of countries after scrapping country names
# Also, it saves a list of countries in .csv file
# We will need .csv file with the country names for the second stage.
list_of_countries = []
for country in countries:
    list_of_countries.append(country.text)
    f = open('1Countries.csv','w', newline='')
    with f:
        writer = csv.writer(f)
        writer.writerow(list_of_countries)

# Closing web browser
time.sleep(2)
driver.quit()
