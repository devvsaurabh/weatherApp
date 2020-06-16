import requests
from flask import Flask, render_template,request,redirect,url_for,flash
from CityList import City_Name

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisseckey'

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=imperial&appid=6d0721dd734ae111e685ced18052e87a'
    r = requests.get(url).json()
    return r

@app.route('/')
def index_get():

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6d0721dd734ae111e685ced18052e87a'
    obj = City_Name()
    cities = obj.get_city()

    weather_data = []

    for city in cities:
        r = get_weather_data(city[0])
        print(r)
    
        weather = {
            'city': city[0],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'wind_speed':r['wind']['speed'],
            'humidity': r['main']['humidity'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(weather)

    return render_template('weather.html',weather_data=weather_data)


@app.route('/', methods=['POST'])
def index_post():
    err_msg = ''
    new_city = request.form.get('city')
    if new_city:
        new_city_obj = City_Name(new_city)
        if new_city_obj.check_existing_city() == 'notexists':
            new_city_data = get_weather_data(new_city)
            if new_city_data['cod'] == 200:
                new_city_obj.add_city()
            else:
                err_msg = 'City does not exist!'
        else:
            err_msg = 'City already exists in the database!'

    if err_msg:
        flash(err_msg,'error')
    else:
        flash("City added successfully!")

    return redirect(url_for('index_get'))


@app.route('/delete/<name>')
def del_city(name):
    city_obj = City_Name(name)
    city_obj.delete_city()
    flash(f'Successfully deleted { name }','success')
    return redirect(url_for('index_get'))



if __name__ == "__main__":
    app.run(debug=True)


