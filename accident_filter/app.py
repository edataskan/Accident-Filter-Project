from flask import Flask, request, jsonify, render_template, g
import mysql.connector

app = Flask(__name__)

# Veritabanı bağlantı ayarları
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '0606',
    'database': 'acci'
}

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
    return g.db

@app.before_request
def before_request():
    g.db = get_db()
    g.cursor = g.db.cursor(dictionary=True)

@app.after_request
def after_request(response):
    g.cursor.close()
    g.db.close()
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accidents', methods=['GET'])
def get_accidents():
    filters = {
        'road_type': request.args.getlist('road_type'),
        'weather_conditions': request.args.getlist('weather_conditions'),
        'accident_severity': request.args.getlist('accident_severity'),
        'light_conditions': request.args.getlist('light_conditions'),
        'urban_or_rural_area': request.args.getlist('urban_or_rural_area'),
        'casualty_severity': request.args.getlist('casualty_severity'),
        'vehicle_type': request.args.getlist('vehicle_type'),
        'sex_of_driver': request.args.getlist('sex_of_driver')
    }

    query = """
    SELECT DISTINCT a.*, v.vehicle_type
    FROM accident a
    LEFT JOIN road r ON a.accident_index = r.accident_index
    LEFT JOIN weather w ON a.accident_index = w.accident_index
    LEFT JOIN lighting l ON a.accident_index = l.accident_index
    LEFT JOIN casualty c ON a.accident_index = c.accident_index
    LEFT JOIN vehicle v ON a.accident_index = v.accident_index
    LEFT JOIN driver d ON v.vehicle_reference = d.vehicle_reference
    WHERE 1=1
    """

    if filters['road_type']:
        road_types_str = ','.join(filters['road_type'])
        query += f" AND r.road_type IN ({road_types_str})"
    if filters['weather_conditions']:
        weather_conditions_str = ','.join(filters['weather_conditions'])
        query += f" AND w.weather_conditions IN ({weather_conditions_str})"
    if filters['accident_severity']:
        accident_severities_str = ','.join(filters['accident_severity'])
        query += f" AND a.accident_severity IN ({accident_severities_str})"
    if filters['light_conditions']:
        light_conditions_str = ','.join(filters['light_conditions'])
        query += f" AND l.light_conditions IN ({light_conditions_str})"
    if filters['urban_or_rural_area']:
        urban_or_rural_area_str = ','.join(filters['urban_or_rural_area'])
        query += f" AND a.urban_or_rural_area IN ({urban_or_rural_area_str})"
    if filters['casualty_severity']:
        casualty_severity_str = ','.join(filters['casualty_severity'])
        query += f" AND c.casualty_severity IN ({casualty_severity_str})"
    if filters['vehicle_type']:
        vehicle_type_str = ','.join(filters['vehicle_type'])
        query += f" AND v.vehicle_type IN ({vehicle_type_str})"
    if filters['sex_of_driver']:
        sex_of_driver_str = ','.join(filters['sex_of_driver'])
        query += f" AND d.sex_of_driver IN ({sex_of_driver_str})"

    g.cursor.execute(query)
    result = g.cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
