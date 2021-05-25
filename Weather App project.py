import requests
from pprint import pprint
from time import sleep

# global scope
cities = {1: "Lagos", 2: "Freetown", 3: "Dakar", 4: "Accra", 5: "Maputo"}


# define a function called WeatherInfo
def get_name():
    print('Welcome to the Weather App for Facade ventures!')

    # Ask for Driver's name
    driver_name = input("What is your name?(format: first name then last name): ")

    # print a welcome mess for the driver
    print("Welcome to Facade ventures, {}!".format(str(driver_name)))
    print(get_city())


# define a function called City
def get_city():
    print('Here are the list of available cities: ')
    for key, value in cities.items():
        print(key, value)

    city_sel = int(input('For information about weather, Kindly select a digit from the options above: '))

    if city_sel == 1:
        city = cities[1]
        print('[INFO] Getting info on Lagos, Nigeria......')

    elif city_sel == 2:
        city = cities[2]
        print('[INFO] Getting info on Freetown, Sierra Leone......')

    elif city_sel == 3:
        city = cities[3]
        print('[INFO] Getting info on Dakar, Senegal......')

    elif city_sel == 4:
        city = cities[4]
        print('[INFO] Getting info on Accra, Ghana......')

    elif city_sel == 5:
        city = cities[5]
        print('[INFO] Getting info on Maputo, Mozambique......')

    else:
        print('ERROR! Kindly select the correct city')

        return city

    # use Open weather app to grab API for weather info of different location
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=429f3e8501f5900ccbe06c8074dbc17b&units=metric".format(
        city)

    req = requests.get(url)
    info = req.json()

    # preparing weather information
    print('[INFO] You have asked for weather information on {}'.format(city))
    sleep(2)
    print('[INFO] Please be patient while we attend to your request...')
    sleep(3)

    # print useful info for the driver
    wind_speed = info['wind']['speed']
    weather_desc = info['weather'][0]['description']
    temp_min = info['main']['temp_min']
    temp_max = info['main']['temp_max']
    feels_like = info['main']['feels_like']
    perc_cloud = info['clouds']['all']
    perc_humidity = info['main']['humidity']
    pressure = info['main']['pressure']
    coord_lat = info['coord']['lat']
    coord_long = info['coord']['lon']

    # Print the format the info should be displayed
    print("Today's Weather Description for is {}".format(weather_desc))
    print('And the weather temperature Feel like {}'.format(feels_like))
    print("The Wind blows at {}m/s".format(wind_speed))
    print('With Latitude {} and Longitude {}'.format(coord_lat, coord_long))
    print('It is also {}% cloudy today in {}'.format(perc_cloud, city))
    print('With a minimum temperature of {} degree celsius'.format(temp_min))
    print('And a maximum Temperature: {} degree celsius'.format(temp_max))
    print('The pressure at {} is {}hPa'.format(city, pressure))
    print('And it is {}% Humid'.format(perc_humidity))


# get_name()

def main():
    get_name()
    get_city()


if __name__ == '__main__':
    main()
