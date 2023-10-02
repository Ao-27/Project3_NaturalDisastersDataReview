import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Disasters_db.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
Base.classes.keys()

app = Flask(__name__)

# Save reference to the table
Disaster = Base.classes.Filtered_Clean_DataAnalysis_NaturalDisasters_1970_2021

@app.route("/")
def welcome():
    return ("The working api route for data is '/api/v1.0/disasters/data'")
        
@app.route("/api/v1.0/disasters/data")
def disasters_data():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    dis_data = session.query(Disaster.TotalDamages, Disaster.TotalDeaths, Disaster.DisNo, Disaster.DisasterGroup, Disaster.DisasterSubgroup,
                            Disaster.DisasterType, Disaster.DisasterSubtype, Disaster.DisasterSubsubtype, Disaster.Country, Disaster.Region,
                            Disaster.Location, Disaster.Continent, Disaster.Start_Date_Complete_Y_N, Disaster.StartYear, Disaster.StartMonth,
                            Disaster.StartDay, Disaster.End_Date_Complete_Y_N, Disaster.EndYear, Disaster.EndMonth, Disaster.EndDay,
                            Disaster.StartDate, Disaster.EndDate, Disaster.StarttoEndDate_DurationDays, Disaster.StarttoEndDate_DurationMonths).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of the disaster information
    disasters_list = []
    for TotalDamages, TotalDeaths, DisNo, DisasterGroup, DisasterSubgroup, DisasterType, DisasterSubtype, DisasterSubsubtype, Country, Region, Location, Continent, Start_Date_Complete_Y_N, StartYear, StartMonth, StartDay, End_Date_Complete_Y_N, EndYear, EndMonth, EndDay, StartDate, EndDate, StarttoEndDate_DurationDays, StarttoEndDate_DurationMonths in dis_data:
        disasters_dict = {}
        
        disasters_dict["Total_Damages"] = TotalDamages
        disasters_dict["Total_deaths"] = TotalDeaths
        disasters_dict["Dis_no"] = DisNo
        disasters_dict["Disaster_group"] = DisasterGroup
        disasters_dict["Disaster_subgroup"] = DisasterSubgroup
        disasters_dict["Disaster_type"] = DisasterType
        disasters_dict["Disaster_subtype"] = DisasterSubtype
        disasters_dict["Disaster_subsubtype"] = DisasterSubsubtype
        disasters_dict["Country"] = Country
        disasters_dict["Region"] = Region
        disasters_dict["Location"] = Location
        disasters_dict["Continent"] = Continent
        disasters_dict["Start_Date_Complete_Y_N"] = Start_Date_Complete_Y_N
        disasters_dict["Start_year"] = StartYear
        disasters_dict["Start_month"] = StartMonth
        disasters_dict["Start_day"] = StartDay
        disasters_dict["End_date_complete_Y_N"] = End_Date_Complete_Y_N
        disasters_dict["End_year"] = EndYear
        disasters_dict["End_month"] = EndMonth
        disasters_dict["End_day"] = EndDay
        disasters_dict["Start_date"] = StartDate
        disasters_dict["End_date"] = EndDate
        disasters_dict["Start_to_end_date_duration_days"] = StarttoEndDate_DurationDays
        disasters_dict["Start_to_end_date_duration_months"] = StarttoEndDate_DurationMonths
       
        disasters_list.append(disasters_dict)

    return jsonify(disasters_list)


if __name__ == '__main__':
    app.run(debug=True)
