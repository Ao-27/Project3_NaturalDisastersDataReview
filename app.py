<<<<<<< HEAD
# Import Dependencies
=======
>>>>>>> 00008b731c46194765c6258952a4179d127c860f
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
<<<<<<< HEAD
from flask_cors import CORS
=======
>>>>>>> 00008b731c46194765c6258952a4179d127c860f

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Disasters_db.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
Base.classes.keys()

<<<<<<< HEAD
# Save reference to the table
# Disaster = Base.classes.Filtered_Clean_DataAnalysis_NaturalDisasters_1970_2021
Disaster_year = Base.classes.disasters_per_year
Final = Base.classes.final

# Flask
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

# api route for main page
@app.route("/")
def welcome():
    return(
        f"Welcome to the Natural Disasters API!<br/>"
        f"Available Routes:<br/>"
        f"The api route for the entire data set is /api/v1.0/disasters/final_data</br>"
        f"The api route for the disasters per year is /api/v1.0/disasters/data/per_year"
    )

# api route for entire data set
@app.route("/api/v1.0/disasters/final_data")
=======
app = Flask(__name__)

# Save reference to the table
Disaster = Base.classes.Filtered_Clean_DataAnalysis_NaturalDisasters_1970_2021

@app.route("/")
def welcome():
    return ("The working api route for data is '/api/v1.0/disasters/data'")
        
@app.route("/api/v1.0/disasters/data")
>>>>>>> 00008b731c46194765c6258952a4179d127c860f
def disasters_data():

    # Create our session (link) from Python to the DB
    session = Session(engine)

<<<<<<< HEAD
    final_data = session.query(Final.country, Final.Total_deaths, Final.Total_Damages, Final.animal_acc, Final.drought, Final.earthquake, Final.epidemic,
                              Final.ex_temp, Final.flood, Final.glacial, Final.impact, Final.insect, Final.lanslide, Final.mass_move, Final.storm,
                              Final.volcano, Final.wildfire, Final.total_dis, Final.lat, Final.lon).all()

    session.close()

    # # Create a dictionary from the row data and append to a list of the entire disasters information
    final_list = []
    for country, Total_deaths, Total_Damages, animal_acc, drought, earthquake, epidemic, ex_temp, flood, glacial, impact, insect, lanslide, mass_move, storm, volcano, wildfire, total_dis, lat, lon in final_data:
        final_dict = {}

        final_dict["Country"] = country
        final_dict["Total_deaths"] = Total_deaths
        final_dict["Total_Damages"] = Total_Damages
        final_dict["animal_acc"] = animal_acc
        final_dict["drought"] = drought
        final_dict["earthquake"] = earthquake
        final_dict["epidemic"] = epidemic
        final_dict["extreme_temp"] = ex_temp
        final_dict["flood"] = flood
        final_dict["glacial"] = glacial
        final_dict["impact"] = impact
        final_dict["insect"] = insect
        final_dict["lanslide"] = lanslide
        final_dict["mass_move"] = mass_move
        final_dict["storm"] = storm
        final_dict["volcano"] = volcano
        final_dict["wildfire"] = wildfire
        final_dict["total_dis"] = total_dis
        final_dict["lat"] = lat
        final_dict["lon"] = lon
    
        final_list.append(final_dict)

    return jsonify(final_list)
                                 

# api route for disasters per year
@app.route("/api/v1.0/disasters/data/per_year")
def disasters_year_data():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    disaster_year = session.query(Disaster_year.Year, Disaster_year.Total_Disasters).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of the total disaster information
    disasters_year_list = []
    for Year, Total_Disasters in disaster_year:
        disasters_year_dict = {}
        
        disasters_year_dict["Year"] = Year
        disasters_year_dict["Total_Disasters"] = Total_Disasters
    
        disasters_year_list.append(disasters_year_dict)

    return jsonify(disasters_year_list)
=======
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
>>>>>>> 00008b731c46194765c6258952a4179d127c860f


if __name__ == '__main__':
    app.run(debug=True)
