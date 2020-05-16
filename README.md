# SeleniumPythonProject

Web scraping of www.openaq.org for open source data to collect air pollution data from different locations in the world. 
Tools used - **Selenium Python**.

I published a blog post about this project on the Towards Data Science blog 
https://towardsdatascience.com/step-by-step-web-scraping-project-using-selenium-in-python-3be887e6e35c

This project was done during the Graduate Studies in Data Science at the University of Warsaw 
together with Jorge Bueno Perez and Noam Shmuel.

## To run the code please run the files with the following sequence:
1. Run **1GetCountries.py** file. The code generates a **1Countries.csv** file which will be used at the Stage 2.
2. Run **2GetLinksOfCountries.p** file. The code generates a **2Links_Of_Countries.csv** file which will be used at the Stage 3.
3. Run **3GetLinksOfCards.py** file. The code generates a **3Links_Of_Cards.csv** file which will be used at the Stage 4.
4. Run **4GetDetails.py** file. The code generates a **4Full_Details.csv** file which will be used at the Stage 5.
5. Run **5GetAnalysis.py** file. The code generates a **5pollution_european_countries.yyyy-mm-dd hh:mm.png** file.
