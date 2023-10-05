# Project3_NaturalDisastersDataReview

### How to Navigate this Repository:


### Introduction to Project:


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

In order to align the data for the HTML visual outputs, the main dataset was joined to Latitudinal and Logitudinal data through python by loading data from this weblink [World Coordinates](https://www.kaggle.com/datasets/parulpandey/world-coordinates "World Coordinates") as a .csv file.

### Data Visualizations:
3 visualizations were produced from the final combined dataset accessed through APIs coordinated via Flask in the app.py and interacted within a browser using the index.html file.

#### The visualizations are titled:
**1. Mapping Out Natural Disasters by Country:**
   * Format Presented: Leaflet Map with Interactive Location Pointers.
   * Content: Each Country displays their: Total Disasters, Total Deaths and Total Damages amounts from the API.
**3. Total Natural Disasters Per Year:**
   * Format Presented: Line Graph with Interactive Total Numbers.
   * Content: Each Year displays their: Total Disasters amount from the API.
**5. Natural Disaster Types by Country:**
   * Format Presented: Pie Chart with Interactive Country Selection Dropdown List.
   * Content: Each Country Selected displays their: Percentage of Total Disaster Types from the API.

## Conclusion:


## Authors:
