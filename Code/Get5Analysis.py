#################################################
###      5. ANALYSING OF POLLUTION LEVELS     ###
###      IN EU COUNTRIES IN 2020 BASED ON     ###
###            THE DATA SCRAPPED              ###
#################################################

# Authors of Code: Lasha Gochiashvili, Noam Shmuel 
# & Jorge Bueno Perez

# Load main packages and libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import time
from time import gmtime, strftime
pd.set_option("display.precision", 2)

'''
In this code we will analyze data that we generated in previous stages.
We want to analyze pollution levels of EU countries in 2020 based on the
data that we generated during scrapping from the website: www.openaq.org

Firstly, we will load results of scrapping as a Data Frame. Then we will
apply data manipulation to clean data. In particular:
-- removing unnecessary columns
-- removing records that have PM 2.5 as 0 or none
-- renaming columns 
-- removing data of non-EU countries

Then we will create boxplot from Seaborn library.
And finally we will save boxplot as a .png.
'''

# Loading results of scrapping as a Data Frame
df = pd.read_csv('4Full_Details.csv')
df = df.dropna()
time.sleep(2)

# Removing unnecessary columns from the table
df.drop(['card_url', 'general', 'city', 'hour', 'country_link'], axis = 1, inplace = True)

time.sleep(2)

# Applying filters to have only records with none zero or non empty
# records on PM2.5 fields.
df = df[df['PM2.5'] > 0]

# Leaving only 2020 data
df = df[df['date'] > '2020/01/01']

# Renaming columns to make it easily readable
df.rename(columns={'country':'Country','PM2.5':'Pollution'}, inplace=True)

# Filtering to leave data only for EU countries
eu_countries = ["Austria", "Belgium", "Czech Republic", "Denmark", "Estonia", "Finland",
                 "France", "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia",
                 "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Netherlands",
                 "Norway", "Poland", "Slovakia", "Portugal", "Slovenia", "Spain", "Sweden", "Switzerland"]

df_eu = df[df['Country'].isin(eu_countries)]

# Creating boxplot from Seaborn library
sns.set(style='ticks', palette='muted', color_codes=True)
plt.figure(figsize=(18, 12))
ax = sns.boxplot(x ='Pollution', y = 'Country', data = df_eu, color = "c")
ax.set_title("Pollution level in EU Countries in 2020", fontsize=30)
sns_plot = sns.stripplot(x = 'Pollution', y = "Country", data=df_eu, jitter=False, size=5, color='.3', linewidth=1)
ax.set_xlabel("Pollution (PM 2.5)",fontsize=15)
ax.set_ylabel("EU Countries",fontsize=15)
sns.despine(trim=True)

time.sleep(2)

# Settings for exporting the boxplot as .png file
time = strftime("%Y-%m-%d %H.%M", gmtime())
fig = sns_plot.get_figure()
fig.savefig("5pollution_european_countries." + time + ".png")
