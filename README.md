# Project3_NaturalDisastersDataReview

### Overview - Introduction to Project:
This project is focused on leveraging Python to complete ETL processes on .csv files to enable APIs through Flask accessing an SQLite database.

The Data within the APIs are presented through HTML and JavaScript visualizations.

As a team we decided to explore our interests in Natural Disasters and to determine if their occurences have increased overtime due to Climate Change. However, as seen in our conclusion we mainly focused on the frequence and impact of the Natural Disasters through our visualizations.

## Getting Started - Data Collection:
The main dataset was sourced from Kaggle.com through this weblink [ALL NATURAL DISASTERS 1900-2021 / EOSDIS](https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis "ALL NATURAL DISASTERS 1900-2021 / EOSDIS") as a .csv file.

By using Python to access the data we found the following columns to be extremely useful for our data visualizations.
*  'Dis No' as Unique ID
*  'Total Damages ('000 US$)'
*  'Total Deaths'
*  'Disaster Type'
*  'Country'
*  'Start/End Year'
*  'Start/End Month'
*  'Start/End Day'
    * We were able to note that there was ~2% of data missing from the Month columns and ~20% for the Day columns.

In order to align the data for the HTML visual outputs, the main dataset was joined to Latitudinal and Logitudinal (location) data through python by loading data from this weblink [World Coordinates](https://www.kaggle.com/datasets/parulpandey/world-coordinates "World Coordinates") as a .csv file.

### Data Visualizations:
3 visualizations were produced from the final combined dataset accessed through APIs coordinated via Flask in the app.py and interacted within a browser using the index.html file.

**The visualizations are titled:**

**1. Mapping Out Natural Disasters by Country:**
   * __Format Presented:__ Leaflet Map with Interactive Location Pointers.
   * __Content:__ Each Country displays their: Total Disasters, Total Deaths and Total Damages amounts from the API.

**2. Total Natural Disasters Per Year:**
   * __Format Presented:__ Line Graph with Interactive Total Numbers.
   * __Content:__ Each Year displays their: Total Disasters amount from the API.

**3. Natural Disaster Types by Country:**
   * __Format Presented:__ Pie Chart with Interactive Country Selection Dropdown List.
   * __Content:__ Each Country Selected displays their: Percentage of Total Disaster Types from the API.

## Conclusion:
The Team was able to notice that we had some lacking datapoints to execute the required depth of analysis to analyze Climate Change impacts. For example, Annual Temperature Averages by Year is not within the main dataset or the location dataset.

Leveraging our location dataset to join with the Country column of the main dataset has enabled us to determine that:
1. The frequency of Natural Diasaters are increasing,
2. Standardized data collection by each country would greatly increase the depth of our analysis,
3. The impact of what data is missing from each Natural Disaster varies over time.

