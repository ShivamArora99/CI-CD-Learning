import json

def process_weather_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    processed_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'weather': data['weather'][0]['description']
    }

    with open(output_file, 'w') as f:
        json.dump(processed_data, f)

if __name__ == "__main__":
    process_weather_data('data/weather.json', 'data/processed_weather_data.json')

