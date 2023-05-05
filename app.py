import requests
import configparser
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('home.html')


@app.route('/results', methods=["POST"])
def render_results():
    city_name = request.form['cityName']
    api_key = get_api_key()
    data = get_weather_results(city_name, api_key)
    
    city = data["city"]["name"]
    country = data["city"]["country"]
    sunup = data["city"]["sunrise"]
    timezone = data["city"]["timezone"]
    sunrise = datetime.utcfromtimestamp(sunup+timezone).strftime("%H:%M")
    sundown = data["city"]["sunset"]
    sunset = datetime.utcfromtimestamp(sundown+timezone).strftime("%H:%M")
    
    #current Weather
    current_temp = round(data["list"][0]["main"]["temp"])
    current_temp_max = round(data["list"][0]["main"]["temp_max"])
    current_temp_min = round(data["list"][0]["main"]["temp_min"])
    current_description = data["list"][0]["weather"][0]["description"]
    current_wind = data["list"][0]["wind"]["speed"]
    current_humidity = data["list"][0]["main"]["humidity"]
    date = data["list"][0]["dt"]
    current_date = datetime.utcfromtimestamp(date).strftime("%A %d %B")
    current_icon_id = data["list"][0]["weather"][0]["icon"]
    current_url = 'https://openweathermap.org/img/wn/{icon}.png'.format(icon=current_icon_id)
                            
    
    #next 5 days weather
    day_one_weather_description = data["list"][8]["weather"][0]["description"]
    day_one_temp = round(data["list"][8]["main"]["temp"])    
    day_one_humidity = data["list"][8]["main"]["humidity"]
    day_one_wind = data["list"][8]["wind"]["speed"]
    date1 = data["list"][8]["dt"]
    day_one_day = datetime.utcfromtimestamp(date1).strftime("%a")
    day_one_date = datetime.utcfromtimestamp(date1).strftime("%d %b")
    day_one_icon_id = data["list"][8]["weather"][0]["icon"]
    day_one_url = 'https://openweathermap.org/img/wn/{icon}.png'.format(icon=day_one_icon_id) 
                            
    
    
    
    day_two_weather_description = data["list"][16]["weather"][0]["description"]
    day_two_temp = round(data["list"][16]["main"]["temp"])  
    day_two_humidity = data["list"][16]["main"]["humidity"]
    day_two_wind = data["list"][16]["wind"]["speed"]
    date2 = data["list"][16]["dt"]
    day_two_day = datetime.utcfromtimestamp(date2).strftime("%a")
    day_two_date = datetime.utcfromtimestamp(date2).strftime("%d %b")
    day_two_icon_id = data["list"][16]["weather"][0]["icon"]
    day_two_url = 'https://openweathermap.org/img/wn/{icon}.png'.format(icon=day_two_icon_id)  
    
    
    
    day_three_weather_description = data["list"][24]["weather"][0]["description"]
    day_three_temp = round(data["list"][24]["main"]["temp"])   
    day_three_humidity = data["list"][24]["main"]["humidity"]
    day_three_wind = data["list"][24]["wind"]["speed"] 
    date3 = data["list"][24]["dt"]
    day_three_day = datetime.utcfromtimestamp(date3).strftime("%a")
    day_three_date = datetime.utcfromtimestamp(date3).strftime("%d %b")
    day_three_icon_id = data["list"][24]["weather"][0]["icon"]
    day_three_url = 'https://openweathermap.org/img/wn/{icon}.png'.format(icon=day_three_icon_id) 
    
    
    day_four_weather_description = data["list"][32]["weather"][0]["description"]
    day_four_temp = round(data["list"][32]["main"]["temp"])   
    day_four_humidity = data["list"][32]["main"]["humidity"]
    day_four_wind = data["list"][32]["wind"]["speed"]
    date4 = data["list"][32]["dt"]
    day_four_day = datetime.utcfromtimestamp(date4).strftime("%a") 
    day_four_date = datetime.utcfromtimestamp(date4).strftime("%d %b")
    day_four_icon_id = data["list"][32]["weather"][0]["icon"]
    day_four_url = 'https://openweathermap.org/img/wn/{icon}.png'.format(icon=day_four_icon_id) 
    
    
    day_five_weather_description = data["list"][39]["weather"][0]["description"]
    day_five_temp = round(data["list"][39]["main"]["temp"])    
    day_five_humidity = data["list"][39]["main"]["humidity"]
    day_five_wind = data["list"][39]["wind"]["speed"]
    date5 = data["list"][39]["dt"]
    day_five_day = datetime.utcfromtimestamp(date5).strftime("%a") 
    day_five_date = datetime.utcfromtimestamp(date5).strftime("%d %b")
    day_five_icon_id = data["list"][39]["weather"][0]["icon"]
    day_five_url = 'https://openweathermap.org/img/wn/{icon}.png'.format(icon=day_five_icon_id) 
    
    
    return render_template("weatherresults.html", city=city, country=country, current_temp=current_temp, 
                           current_temp_max=current_temp_max, current_temp_min= current_temp_min, 
                           current_description=current_description, current_wind=current_wind, 
                           current_humidity=current_humidity, current_date=current_date, sunrise=sunrise, sunset=sunset,
                           current_url=current_url,
                           
                           day_one_weather_description=day_one_weather_description, day_one_temp=day_one_temp,
                           day_one_humidity=day_one_humidity, day_one_wind=day_one_wind,
                           day_one_date=day_one_date, day_one_day=day_one_day, day_one_url=day_one_url,
                           
                           day_two_weather_description=day_two_weather_description, day_two_temp=day_two_temp,
                           day_two_humidity=day_two_humidity, day_two_wind=day_two_wind,
                           day_two_day=day_two_day, day_two_date=day_two_date, day_two_url=day_two_url,
                           
                           day_three_weather_description=day_three_weather_description, day_three_temp=day_three_temp,
                           day_three_humidity=day_three_humidity, day_three_wind=day_three_wind, 
                           day_three_day=day_three_day, day_three_date=day_three_date, day_three_url=day_three_url,
                           
                           day_four_weather_description=day_four_weather_description, day_four_temp=day_four_temp,
                           day_four_humidity=day_four_humidity, 
                           day_four_wind=day_four_wind, day_four_day=day_four_day, day_four_date=day_four_date,
                           day_four_url=day_four_url,
                           
                           day_five_weather_description=day_five_weather_description, day_five_temp=day_five_temp,
                           day_five_humidity=day_five_humidity, day_five_wind=day_five_wind,
                           day_five_day=day_five_day, day_five_date=day_five_date, day_five_url=day_five_url)

def get_api_key():
    config= configparser.ConfigParser()
    config.read("config.ini")
    return config['Openweathermap']['api']

def get_weather_results(city_name, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}".format(city_name, api_key)
    request = requests.get(api_url)
    return request.json()

if __name__ == '__main__':
    app.run()

