import requests
import csv
from flask import Flask,jsonify

app = Flask(__name__)

def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        with open('data.csv', 'wb') as file:
            file.write(content)
        print("File downloaded successfully.")
        
        # Read the downloaded CSV file
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print("Failed to download the file.")

# Test the function with the given URL
url = "https://corgis-edu.github.io/corgis/datasets/csv/weather/weather.csv"

#download_data(url)
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(dict(row))
    return data

# Example usage
file_path = 'data.csv'
data = load_data(file_path)
#print(data)

def analyze_data(data):
    max_temperature = float('-inf')
    min_temperature = float('inf')
    total_temperature = 0
    temperature_count = 0
    location_with_most_heat = None
    
    for row in data:
        temperature = float(row['temperature'])
        
        # Update maximum temperature
        if temperature > max_temperature:
            max_temperature = temperature
            location_with_most_heat = row['location']
        
        # Update minimum temperature
        if temperature < min_temperature:
            min_temperature = temperature
        
        # Calculate total temperature and count
        total_temperature += temperature
        temperature_count += 1
    
    average_temperature = total_temperature / temperature_count
    
    analysis = {
        'max_temperature': max_temperature,
        'min_temperature': min_temperature,
        'average_temperature': average_temperature,
        'location_with_most_heat': location_with_most_heat
    }
    
    return analysis

# Example usage
data = [
    {'location': 'A', 'temperature': '30'},
    {'location': 'B', 'temperature': '35'},
    {'location': 'C', 'temperature': '32'},
    {'location': 'D', 'temperature': '28'},
    {'location': 'E', 'temperature': '33'}
]


#print(result)
#rest api
@app.route('/weather/download', methods=['POST'])
def download_endpoint():
    try:
        download_data(url)
        response = {
            'status': 'success',
            'message': 'Weather data download triggered successfully'
        }
        
        status_code = 200
    except Exception as e:
        response = {
            'status': 'error',
            'message': 'Failed to trigger weather data download',
            'error': str(e)
        }
        status_code = 500
    return jsonify(response), status_code

@app.route('/weather/update', methods=['POST'])
def update_weather_analysis():
    try:
        result = analyze_data(data)
        
        response = {
            'status': 'success',
            'message': 'Weather analysis updated successfully'
        }
        status_code = 200
    
    except Exception as e:
        
        response = {
            'status': 'error',
            'message': 'Failed to update weather analysis',
            'error': str(e)
        }
        status_code = 500
    
    return jsonify(response), status_code

@app.route('/weather/report', methods=['GET'])    
def get_weather_report():
    try:
        result = analyze_data(data) 
        # Placeholder response
        response = {
            'status': 'success',
            'data': result
        }
        status_code = 200
    
    except Exception as e:
        # Handle the specific exception types you expect to occur
        
        # Placeholder error response
        response = {
            'status': 'error',
            'message': 'Failed to fetch weather analysis report',
            'error': str(e)
        }
        status_code = 500
    
    return jsonify(response), status_code

@app.route('/weather/report/average_temperature', methods=['GET'])
def get_average_temperature():
    try:
        result = analyze_data(data)
        average_temperature = result['average_temperature']
        
        # Placeholder response
        response = {
            'status': 'success',
            'average_temperature': average_temperature
        }
        status_code = 200
    
    except Exception as e:
        # Handle the specific exception types you expect to occur
        
        # Placeholder error response
        response = {
            'status': 'error',
            'message': 'Failed to fetch average temperature',
            'error': str(e)
        }
        status_code = 500
    
    return jsonify(response), status_code

@app.route('/weather/report/max_temperature', methods=['GET'])
def get_max_temperature():
    try:
        result = analyze_data(data)
        max_temperature = result['max_temperature']
        
        # Placeholder response
        response = {
            'status': 'success',
            'max_temperature': max_temperature
        }
        status_code = 200
    
    except Exception as e:
        # Handle the specific exception types you expect to occur
        
        # Placeholder error response
        response = {
            'status': 'error',
            'message': 'Failed to fetch max temperature',
            'error': str(e)
        }
        status_code = 500
    
    return jsonify(response), status_code

@app.route('/weather/report/min_temperature', methods=['GET'])
def get_min_temperature():
    try:
        result = analyze_data(data)
        min_temperature = result['min_temperature']
        
        # Placeholder response
        response = {
            'status': 'success',
            'min_temperature': min_temperature
        }
        status_code = 200
    
    except Exception as e:
        # Handle the specific exception types you expect to occur
        
        # Placeholder error response
        response = {
            'status': 'error',
            'message': 'Failed to fetch min temperature',
            'error': str(e)
        }
        status_code = 500
    
    return jsonify(response), status_code


@app.route('/weather/report/location_with_most_heat', methods=['GET'])
def get_location_with_most_heat():
    try:
        result = analyze_data(data)
        location_with_most_heat = result['location_with_most_heat']
        
        # Placeholder response
        response = {
            'status': 'success',
            'location_with_most_heat': location_with_most_heat
        }
        status_code = 200
    
    except Exception as e:
        # Handle the specific exception types you expect to occur
        
        # Placeholder error response
        response = {
            'status': 'error',
            'message': 'Failed to fetch location_with_most_heat',
            'error': str(e)
        }
        status_code = 500
    
    return jsonify(response), status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)