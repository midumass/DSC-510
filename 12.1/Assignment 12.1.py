# DSC510-T301 Assignment 12.1
# Zachary Hill
# 02MAR2019
# Final Project
# This program calls OpenWeather.org's weather API
# Locations are prompted from user, analyzed for relevant type of call
# and results are returned in a readable format.

import requests
import json
import datetime

loc = ''
country = ''
print("Welcome to OpenWeather's API forecaster")


# Validates whether the input is a number or not, returns true/false
def zipTest(userInput):
    try:
        int(userInput)
        return True
    except:
        return False

# Validates whether the zip code entered is valid, returns location or prompts to try again
def validateLoc():
    global loc
    loc = input('Enter your 5-digit zip code or city: ')
    if zipTest(loc) == True:
        if len(loc) == 5:
            return loc
        else:
            print('This is not a valid zip code')
            validateLoc()
            return loc
    else:
        return loc

# Validates whether the entered country code is valid, and passes US back if zip code is entered
def validateCountry():
    global country
    if zipTest(loc) == False:
        country = input('Enter your 2 character country code (eg, US): ')
        if len(country) == 2:
            return country
        else:
            print('This is not a valid country code code')
            validateCountry()
            return country
    else:
        country = 'US'
        return country

# Uses wind direction to output cardinal direction of wind, returns more readable output
def cardinalDirection(degrees):
    if 22 <= degrees < 67:
        return str('NE')
    elif 67 <= degrees < 112:
        return str('E')
    elif 112 <= degrees < 157:
        return str('SE')
    elif 157 <= degrees < 202:
        return str('S')
    elif 202 <= degrees < 247:
        return str('SW')
    elif 247 <= degrees < 292:
        return str('W')
    elif 292 <= degrees < 337:
        return str('NW')
    else:
        return str('N')

# Handles status return codes from API call, return based on status code
def statusHandler(responseStatus):
    if responseStatus.status_code == 200:
        success = json.loads(responseStatus.content.decode('utf-8'))
        return success
    elif responseStatus.status_code == 404:
        print('The location you are requesting was not found, please try again.')
        return callWeatherAPI(validateLoc(), validateCountry())
    else:
        print(responseStatus)

# Calls Weather API, tests whether zip or city, changes API based on input, returns response from statusHandler
def callWeatherAPI(zipCity, cCode):
    apiCall = 'http://api.openweathermap.org/data/2.5/weather?{loc}={zc},{cc}&APPID=b8241b03fb8d18766a2035cbab56e2e1'
    try:
        if zipTest(zipCity) == True:
            response = requests.get(apiCall.format(loc='zip', zc=zipCity, cc=cCode))
        else:
            response = requests.get(apiCall.format(loc='q', zc=zipCity, cc=cCode))
        return statusHandler(response)
    except:
        print('The Weather API failed to respond. Please try again later')

# Asks user to input whether they want to try another city
def repeatMain():
    yes = ('yes', 'y', 'ya', 'si', 'ja', 'hai', 'ye')
    restart = input('Would you like to check another loction?').lower()
    if restart in yes:
        main()
    else:
        print('Thank you for using Zach\'s weather app.')
        exit()

# Makes for pretty output
def prettyPrint(weatherResults):
    location = weatherResults['name']
    conditions = weatherResults["weather"][0]
    figures = weatherResults['main']
    wind = weatherResults['wind']
    direction = cardinalDirection(wind['deg'])
    fahrenheit = "{:.1f}".format(((9 * (figures['temp'] - 273)) / 5) + 32)
    print('Currently we see', conditions['description'], 'in', location)
    print("{:<14} {:>24}".format('Temperature:', str(fahrenheit) + '\u00b0' + 'F'))
    print("{:<14} {:>24}".format('Humidity:', str(figures['humidity']) + '\u0025'))
    print("{:<14} {:>24}".format('Wind Speed:', str(wind['speed']) + " mph " + direction))
    print("{:<14} {:>24}".format('Sunrise:', datetime.datetime.fromtimestamp(weatherResults['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')))
    print("{:<14} {:>24}".format('Sunset:', datetime.datetime.fromtimestamp(weatherResults['sys']['sunset']).strftime(
        '%Y-%m-%d %H:%M:%S')))

# Main function
def main():
    results = callWeatherAPI(validateLoc(), validateCountry())
    prettyPrint(results)
    repeatMain()


main()
