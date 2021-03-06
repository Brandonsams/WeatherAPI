import webbrowser

class zipURL:
    def __init__(self,key,zipCode,domain = 'api.openweathermap.org',path = '/data/2.5/forecast'):
        self.key = key
        self.zip = zipCode
        self.domain = domain
        self.path = path
    
    def __str__(self):
        return(f'{self.domain}{self.path}?zip={self.zip}&appid={self.key}')

class cityURL:
    def __init__(self,key,city,country = 'us',domain = 'api.openweathermap.org',path = '/data/2.5/forecast'):
        self.key = key
        self.city = city
        self.domain = domain
        self.path = path
    
    def __str__(self):
        return(f'{self.domain}{self.path}?q={self.city}&appid={self.key}')

key = '1be0090c214feacb5b1622d1012b499f'
zipCode = 97030
city = 'Portland'

forecastURL = zipURL(key,zipCode)
print(forecastURL.key)
print(forecastURL.__dict__)
print(forecastURL)

# http://api.openweathermap.org/data/2.5/forecast?q=Portland&appid=1be0090c214feacb5b1622d1012b499f