# Accident-Filter Project

In this project I used a dataset that I found from kaggled.This dataset has some data about accidents that took place in the UK between 1979 and 2015 (For example, the gender of the person who caused the accident, the condition of the road, the condition of the injured person).I pulled these features from the database I created in mysql and coded a filtering system.This website will list the accidents according to the features in the filter you choose.

I created some tables to use these filtering systems in mysql.You can find these codes in the file.I also found csvs according to the features I created in the tables in order to use the datasets I found from kaggle more effectively.I also uploaded these csv files.But in order to run this project, you must first integrate the data in the csv into the tables.


# Features

- Retrieve accident data with multiple filtering options.
- Integrates with a MySQL database to fetch the relevant data.
- Simple web interface to access the API.

## Installation

### Requirements

- Python 3.x
- Flask
- MySQL database
- MySQL Connector for Python

### Steps

1. Navigate to the Project Directory
    Change your current directory to the project's directory:

    cd /path/to/your/project

2. Set up a virtual environment and install dependencies:

    python -m venv myvenv

    myvenv\Scripts\activate

    pip install Flask mysql-connector-python
    
    
3. Start the development server:

    python app.py 
    

