create database acci ;
USE acci;

CREATE TABLE road (
    road_type INT,
    speed_limit INT,
    junction_detail INT,
    junction_control INT,
    accident_index DOUBLE,
    road_surface_conditions TINYINT
);

CREATE TABLE weather (
    weather_conditions INT,
    accident_index DOUBLE
);

CREATE TABLE accident (
    accident_index VARCHAR(255) PRIMARY KEY,
    date DATE,
    time DATETIME,
    police_force INT,
    accident_severity INT,
    number_of_vehicles INT,
    number_of_casualties INT,
    urban_or_rural_area INT,
    did_police_officer_attend_scene_of_accident INT,
    day_of_week TINYINT
);


CREATE TABLE lighting (
    accident_index DOUBLE,
    light_conditions INT
);


CREATE TABLE location (
    accident_index DOUBLE,
    location_easting_osgr INT,
    location_northing_osgr INT,
    longitude INT,
    latitude INT
);

CREATE TABLE casualty (
    sex_of_casualty INT,
    age_of_casualty INT,
    casualty_severity INT,
    accident_index DOUBLE,
    casualty_type INT,
    casualty_home_area_type TINYINT,
    car_passenger TINYINT,
    age_band_of_casualty INT
);

CREATE TABLE driver (
    sex_of_driver INT,
    age_of_driver INT,
    age_band_of_driver INT,
    vehicle_reference INT
);

CREATE TABLE vehicle (
	vehicle_reference INT PRIMARY KEY,
    vehicle_type INT,
    engine_capacity_cc INT,
    propulsion_code TINYINT,
    age_of_vehicle INT,
    driver_id INT,
    accident_index DOUBLE,
    vehicle_manoeuvre INT,
    skidding_and_overturning INT,
    1st_point_of_impact TINYINT
);


CREATE TABLE vehicle_manoeuvre (
    vehicle_manoeuvre INT,
    vehicle_reference INT
);
CREATE TABLE vehicle_location (
    vehicle_location_restricted_lane TINYINT,
    vehicle_reference INT
);

