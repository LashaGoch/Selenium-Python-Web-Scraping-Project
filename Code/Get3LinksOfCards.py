#################################################
###     3. GET THE LINKS OF THE CARDS         ###
###              OF EACH PAGE                 ###
#################################################

# NOTE: This code takes around 15 mins runtime due to 
# the wait time in getCardUrl function which is 
# necessary to scrap data from each location card.

# Authors of Code: Noam Shmuel & Lasha Gochiashvili
# Load main packages and libraries
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver settings
gecko_path = 'C:/Users/Lasha/anaconda3/geckodriver.exe'

options = webdriver.firefox.options.Options()
options.headless = True
driver = webdriver.Firefox(options = options, executable_path = gecko_path)

driver.implicitly_wait(5)

'''
We created this function to use links of each country page that 
we stored in previous stage and scrap the urls for each cards 
inside the country page. Then saving the card urls that we will 
use at the next stage to access inside card and get the data about 
pollution in each location.
'''
def getCardUrl(country, url):
    driver.get(url)
    local_df = pd.DataFrame(columns=['country','country_url', 'cardURL'])
    
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card__title')))
        titles = driver.find_elements_by_css_selector('.card__title [href]')
        # scraping urls of location cards by "css_selector"

        for title in titles:
            time.sleep(1)
            try:
                card_link = (title.get_attribute('href'))
                d = {'country':country, 'country_url':url, 'cardURL':card_link}
                local_df = local_df.append(d, ignore_index=True)
                # Saving srapped urls into the Data Frame
            except:
                d = {'country':country, 'country_url':url, 'cardURL':None}
                local_df = local_df.append(d, ignore_index=True) 
    except:
        d = {'country':country, 'country_url':url, 'cardURL':None}
        local_df = local_df.append(d, ignore_index=True)
    
    return (local_df)

time.sleep(2)

'''
Loading Data Frame of country & country_url that we created
at the previous stage. We will add now scrapped urls of each 
location card that we get from each country page.
'''
df = pd.read_csv('2Links_Of_Countries.csv')
df2 = pd.DataFrame(columns=['country','country_url', 'cardURL'])

for index, row in df.iterrows():
    myDf = pd.DataFrame(columns=['country','country_url', 'cardURL'])
    country_url = (row['country_url'])
    country = (row['country'])
    myDf = getCardUrl(country, country_url)
    df2 = df2.append(myDf, ignore_index=True)
    
# Printing Data Frame of country, country_url and location card url.
print(df2)
time.sleep(2)

# Saving created Data Frame into .csv file
df2.to_csv('3Links_Of_Cards.csv', index=False, header=True)

# Closing web browser
time.sleep(2)
driver.quit()
