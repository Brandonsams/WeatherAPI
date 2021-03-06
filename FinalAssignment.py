'''
File: FinalAssignment.py
Name: Brandon Sams
Date: 16November2019
Course: DSC510 - Intro to Programming
Description: Gets 5-Day Weather Forecast
Usage: User will supply a city or zip code, and a formatted forecast will return as a table
'''

import requests
from requests.exceptions import HTTPError
import json
import datetime

class zipURL:
    # url object that includes the zip code that was provided by the user
    def __init__(self, zipCode, key='1be0090c214feacb5b1622d1012b499f', protocol='https://', domain='api.openweathermap.org', path='/data/2.5/forecast'):
        # Initialize parts of the url
        self.key = key
        self.zip = zipCode
        self.protocol = protocol
        self.domain = domain
        self.path = path

    def __str__(self):
        # puts the parts of the url together into one string
        return(f'{self.protocol}{self.domain}{self.path}?zip={self.zip}&appid={self.key}')

    def getForecast(self):
        # attempt to get json weather response
        try:
            print(f'Getting Weather for {self.zip}...')
            resp = requests.get(self)
            resp.raise_for_status()
            # Raises and stores HTTPError, if one occurred
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return('')
        except Exception as err:
            print(f'Other error occurred: {err}')
            return('')
        else:
            return(resp.json())
            # Response was successful. Send it on.


class cityURL:
    # url object that includes the city that was provided by the user
    def __init__(self, city, key='1be0090c214feacb5b1622d1012b499f', protocol='https://', domain='api.openweathermap.org', path='/data/2.5/forecast'):
        # Initialize the parts of the url
        self.key = key
        self.city = city
        self.protocol = protocol
        self.domain = domain
        self.path = path

    def __str__(self):
        # return url as a string
        return(f'{self.protocol}{self.domain}{self.path}?q={self.city}&appid={self.key}')

    def getForecast(self):
        # attempt to get json weather response
        try:
            print(f'Getting Weather for {self.city}...')
            resp = requests.get(self)
            resp.raise_for_status()
            # Raises and stores HTTPError, if one occurred
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return('')
        except Exception as err:
            print(f'Other error occurred: {err}')
            return('')
        else:
            return(resp.json())
            # Forecast request was successful. Send it on.

def getForecastURL():
    location = promptZipOrCity()
    # prompt the user for a location
    try:
        zipCode = int(location)
        # if the location provided is an integer, it must be a zip code
        url = zipURL(zipCode)
        return(url)
    except:
        city = location
        # location must be a city
        url = cityURL(city)
        return(url)

def promptZipOrCity():
    location = input('Please provide either a zip code or a city in the United States.\n')
    return(location)

def getWeatherLists(forecast):
    dateTimeList = []
    tempList = []
    weatherConditionList = []
    # make a bunch of empty lists. Add to them later.

    for item in forecast['list']:
    # Loop through json forecast

        datetimeUTC = item['dt']
        datetimeLocalUTC = int(datetimeUTC) + int(forecast['city']['timezone'])
        dateShort = datetime.datetime.utcfromtimestamp(datetimeLocalUTC).strftime("%a %I %p")
        dateTimeList.append(dateShort)
        # Append formatted datetime to list

        kelvin = float(item['main']['temp'])
        fahrenheit = (kelvin*(9/5))-459.67
        tempList.append(fahrenheit)
        # Append temperature in fahrenheit to list

        weather = item['weather'][0]['description']
        weatherConditionList.append(weather)
        # Append weather condition to list

    return(dateTimeList,tempList,weatherConditionList)

def prettyPrintForecast(dates,temps,conditions):
    maxConditionLength = len(max(conditions+['Conditions'], key=len))
    # Weather condition string can vary in length. Use for making pretty table
    printForecastHeader(maxConditionLength)
    # Title row
    for i in range(len(dates)):
        if dates[i][:3] != dates[i-1][:3]:
        # is it a new day? Put a line in.
            bufferDashes = '-' * maxConditionLength
            print(f'+-----------+----+-{bufferDashes}-+')
        bufferspace = " "*(maxConditionLength-len(conditions[i]))
        forecastString = f"| {dates[i]} | {round(temps[i])} | {conditions[i]}{bufferspace} |"
        print(forecastString)
        # Print forecast as a line of the table
    printForecastFooter(maxConditionLength)
    # cap off the table

def printForecastHeader(maxConditionLength):
    bufferDashes = '-' * maxConditionLength
    bufferSpaces = ' ' * (maxConditionLength-10)
    degree = u"\u00b0"
    # Degree symbol
    print(f'+-----------+----+-{bufferDashes}-+')
    print(f'| DateTime  | {degree}F | Conditions{bufferSpaces} |')

def printForecastFooter(maxConditionLength):
    bufferDashes = '-' * maxConditionLength
    print(f'+-----------+----+-{bufferDashes}-+')

def forecastAgain():
    # Display menu to user. Let them ask for weather again or not
    again = input('Would you like to check the weather again?\n\t(y) Yes\n\t(n) No\n')
    if again.lower() == 'y':
        return('y')
    elif again.lower() == 'n':
        return('n')
    else:
        print('Invalid Input. Try again.')
        again = forecastAgain()
        return(again)

def main():
    url = getForecastURL()
    # makes url object
    forecast = url.getForecast()
    # query API for openweathermap.com
    if len(forecast) > 0:
        # the forecast was successfully returned
        dates,temps,conditions = getWeatherLists(forecast)
        # parse the json
        prettyPrintForecast(dates,temps,conditions)
        # print as a nice table
    again = forecastAgain()
    if again == 'y':
        main()
        # Ask for more weather!
    
main()

