# Import the dependencies.

import json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, request

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model

Base = automap_base()

# reflect the tables

Base.prepare(autoload_with=engine)

# Save references to each table
Data = Base.classes.data

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route(“/”)
def first_page():
    print(“Whatever you want to show up on your end when someone accesses the server(?)”)
    return “Here are all the available routes…”


@app.route(“/api/v1.0/precipitation”)
def precipitation():
    return jsonify()


@app.route(“/api/v1.0/stations”)
def station_list():
    return jsonify()


@app.route(“/api/v1.0/tobs”)
def temp_observations():
    return jsonify(“List of temperature observations for the previous year”)


@app.route(“/api/v1.0<start>)
def min_ave_max_temps():
    return jsonify()

@app.route(“/api/v1.0/<start>/<end>”)
def 
Return jsonify(“”)

if __name__ == "__main__":
    app.run(debug=True)