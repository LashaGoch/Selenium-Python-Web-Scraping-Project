#################################################
###     2. GET THE LINKS OF EACH PAGE         ###
###             OF EACH COUNTRY               ###
#################################################

# Author of Code: Noam Shmuel & Lasha Gochiashvili
# Load main packages and libraries
from selenium import webdriver
import pandas as pd
import csv
import time

# Webdriver settings
gecko_path = 'C:/Users/Lasha/anaconda3/geckodriver.exe'

options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options=options, executable_path=gecko_path)

url = 'https://openaq.org/#/locations?parameters=pm25&_k=bmrxjw'
driver.get(url)
time.sleep(2)

# This function opens .csv file that we created at the first stage
# .csv file includes names of countries
with open('1Countries.csv', newline='') as f:
    reader = csv.reader(f)
    list_of_countries = list(reader)
    list_of_countries = list_of_countries[0]
    print(list_of_countries) # printing a list of countries

# Let's create Data Frame of the country & country_url
df = pd.DataFrame(columns=['country', 'country_url'])

# With this function we are generating urls for each country page
for country in list_of_countries[:92]:
	try:
		path = ('//span[contains(text(),' + '\"' + country + '\"' + ')]')
		# "path" is used to filter each country on the website by
		# iterating country names.
		next_button = driver.find_element_by_xpath(path)
		next_button.click()
		# Using "button.click" we are get on the page of next country
		time.sleep(2)
		country_url = (driver.current_url)
		# "country_url" is used to get the url of the current page
		next_button.click()
	except:
		country_url = None

	d = [{'country': country, 'country_url': country_url}]
	df = df.append(d)
	# After getting urls of each country page, we are saving
	# in the Data Frame the we created above the function

# Printing Data Frame
print(df)

# Saving created Data Frame in .csv file which will be used
# at the third stage to get the links of the card on each
# country pages
df.to_csv('2Links_Of_Countries.csv', index=False, header=True)

# Closing web browser
time.sleep(4)
driver.quit()
