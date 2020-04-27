#################################################
###        4. GET THE DETAILS FROM            ###
###               OF EACH CARD                ###
#################################################

# NOTE: this code takes around 20 mins runtime
# due to the number of pages to scrap.

# Authors of Code: Noam Shmuel & Lasha Gochiashvili

# Load main packages and libraries
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver settings
gecko_path = 'C:/Users/Lasha/anaconda3/geckodriver.exe'

options = webdriver.firefox.options.Options()
options.headless = True

driver = webdriver.Firefox(options = options, executable_path = gecko_path)

'''
By this function we will create a Data Frame to save full details 
of scrapping step by step. There are four parts of the function.
'''
def getCardDetails(country, url):
    ### PART I
    # Declaring variables to save the results of scraping
    driver.get(url)
    local_df = pd.DataFrame(columns=['country','card_url','general','country_link','city', 'PM2.5','date','hour'])
    pm = None
    date = None
    hour = None
    general = None
    city = None
    country_link = None
    
    try:
        #wait = WebDriverWait(driver, 3)
        #wait.until(EC.presence_of_element_located((By.ID, 'location-fold-stats')))
        time.sleep(2)

        ### PART II
        # Using Xpath we are getting the full text of the sibling that comes
        # after the text containing "PM2.5". We will split the full text to
        # generate variables for our Data Frame such as "pm", "date" & "hour".
        try:
            pm_date = driver.find_element(By.XPATH, '//dt[text() = "PM2.5"]/following-sibling::dd[1]').text
            # Scraping pollution details from each location page
            # and splitting them to save in the relevant variables
            text = pm_date.split('µg/m³ at ')
            pm = float(text[0])
            full_date = text[1].split(' ')
            date = full_date[0]
            hour = full_date[1]
        except:
            pm = None
            date = None
            hour = None

        ### PART III
        # Using class name we are getting the full text to generate variables
        # for our Data Frame such as "country", "card_url", "general", "city"
        # & "country_link".
        try:
            titles = driver.find_element_by_class_name('inpage__title').text
            # Scrapping location details and creating variables
            titles_split = titles.split('\n')
            general = titles_split[0]
            titles_split = titles_split[1].split('in ')[1].split(' ')
            city = titles_split[0]
            country_link = titles_split[1]
        except:
            general = None
            city = None
            country_link = None
    except:
        print ("Something went wrong with WAIT")

    ### PART IV
    # Saving each variables that we created into the Data Frame
    d = {'country':country,'card_url':url, 'general':general,'country_link':country_link,'city':city, 'PM2.5':pm,'date':date,'hour':hour }
    local_df = local_df.append(d, ignore_index=True)
    return (local_df)            

time.sleep(2)

# Open the .csv file to use links in order to fill our new Data Frame
# with all the necessary information
df = pd.read_csv('3Links_Of_Cards.csv')
df = df.dropna() # Remove NAs
#print(df)
time.sleep(2)

# Creating Data Frame and setting column names
df2 = pd.DataFrame(columns=['country','card_url','general','country_link','city', 'PM2.5','date','hour'])

# Adding country, country_url and cardURL to the Data Frame
for index, row in df.iterrows():
    myDf = pd.DataFrame(columns=['country','card_url','general','country_link','city', 'PM2.5','date','hour'])
    card_url = (row['cardURL'])
    country = (row['country'])
    time.sleep(1)    
    myDf = getCardDetails(country, card_url)
    df2 = df2.append(myDf, ignore_index=True)
    
# Printing our new Data Frame
print("\n")
print(df2)

# Exporting our new Data Frame with full details as a .csv file
df2.to_csv('4Full_Details.csv', index=False, header=True)

# Closing web browser
time.sleep(2)
driver.quit()
