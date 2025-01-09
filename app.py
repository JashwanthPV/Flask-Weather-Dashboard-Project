from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your OpenWeatherMap API key
API_KEY = '331d562701ba089f2a4bd75394d96047'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Weather data route
@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data['cod'] == '404':
        return render_template('result.html', error="City Not Found")
    else:
        main_data = data['main']
        weather_data = data['weather'][0]
        wind_data = data['wind']

        weather_info = {
            'city': city,
            'temp': main_data['temp'],
            'humidity': main_data['humidity'],
            'description': weather_data['description'],
            'wind_speed': wind_data['speed'],
        }
        return render_template('result.html', weather=weather_info)

if __name__ == "__main__":
    app.run(debug=True)
