import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Disasterdb.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
Base.classes.keys()

# Save reference to the table
Disaster = Base.classes.Disasters

app = Flask(__name__)

@app.route("/")
def welcome():
    
    return ("The working api route for data is '/api/v1.0/disasters/data'")
        
@app.route("/api/v1.0/disasters/data")
def disasters_data():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    dis_data = session.query(Disaster.Total_Damages, Disaster.Total_deaths, Disaster.Dis_no, Disaster.Disaster_group, Disaster.Disaster_subgroup,
                            Disaster.Disaster_type, Disaster.Disaster_subtype, Disaster.Disaster_subsubtype, Disaster.Country, Disaster.Region,
                            Disaster.Location, Disaster.Continent, Disaster.Start_date_complete_Y_N, Disaster.Start_year, Disaster.Start_month,
                            Disaster.Start_day, Disaster.End_date_complete_Y_N, Disaster.End_year, Disaster.End_month, Disaster.End_day,
                            Disaster.Start_date, Disaster.End_date, Disaster.Start_to_end_date_duration_days, Disaster.Start_to_end_date_duration_months).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of the disaster information
    disasters_list = []
    for Total_Damages, Total_deaths, Dis_no, Disaster_group, Disaster_subgroup, Disaster_type, Disaster_subtype, Disaster_subsubtype, Country, Region, Location, Continent, Start_date_complete_Y_N, Start_year, Start_month, Start_day, End_date_complete_Y_N, End_year, End_month, End_day, Start_date, End_date, Start_to_end_date_duration_days, Start_to_end_date_duration_months in dis_data:
        disasters_dict = {}
        
        disasters_dict["Total_Damages"] = Total_Damages
        disasters_dict["Total_deaths"] = Total_deaths
        disasters_dict["Dis_no"] = Dis_no
        disasters_dict["Disaster_group"] = Disaster_group
        disasters_dict["Disaster_subgroup"] = Disaster_subgroup
        disasters_dict["Disaster_type"] = Disaster_type
        disasters_dict["Disaster_subtype"] = Disaster_subtype
        disasters_dict["Disaster_subsubtype"] = Disaster_subsubtype
        disasters_dict["Country"] = Country
        disasters_dict["Region"] = Region
        disasters_dict["Location"] = Location
        disasters_dict["Continent"] = Continent
        disasters_dict["Start_date_complete_Y_N"] = Start_date_complete_Y_N
        disasters_dict["Start_year"] = Start_year
        disasters_dict["Start_month"] = Start_month
        disasters_dict["Start_day"] = Start_day
        disasters_dict["End_date_complete_Y_N"] = End_date_complete_Y_N
        disasters_dict["End_year"] = End_year
        disasters_dict["End_month"] = End_month
        disasters_dict["End_day"] = End_day
        disasters_dict["Start_date"] = Start_date
        disasters_dict["End_date"] = End_date
        disasters_dict["Start_to_end_date_duration_days"] = Start_to_end_date_duration_days
        disasters_dict["Start_to_end_date_duration_months"] = Start_to_end_date_duration_months
       
        disasters_list.append(disasters_dict)
    return jsonify(disasters_list)


if __name__ == '__main__':
    app.run(debug=True)
