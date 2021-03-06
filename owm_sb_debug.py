import json
import owm_sb as o


key = '1be0090c214feacb5b1622d1012b499f'
zipCode = 97030
countryCode = 'US'

url = "https://api.openweathermap.org/data/2.5/weather?zip={0},{1}&appid={2}".format(zipCode,countryCode,key)


forecast = o.request(url)

print(json.dumps(forecast,indent = 4))
print(forecast.keys())