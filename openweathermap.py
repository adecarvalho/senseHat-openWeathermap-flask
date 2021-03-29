import configparser
import requests


class OpenWeatherMap(object):

    def __init__(self):
        self.datas = {}
        self.city = ''
        self.apikey = ''
        self.getApiKey()

    def getApiKey(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.apikey = config['openweathermap']['api_key']

    def fetchDatas(self, _city):
        OPENWEATHER_BEGIN = 'http://api.openweathermap.org/data/2.5/weather?q='
        OPENWEATHER_END = '&appid=' + self.apikey
        OPENWEATHER_LANG_METRIC = '&lang=fr&units=metric'

        OPENWEATHER_ICON_BEGIN='http://openweathermap.org/img/wn/'
        OPENWEATHER_ICON_END='@2x.png'
        
        self.city = _city
        url = OPENWEATHER_BEGIN + self.city + OPENWEATHER_END + OPENWEATHER_LANG_METRIC

        values = requests.get(url).json()

        if values['cod'] == '404':
            self.datas['errors'] = values['message']
            return False
        else:
            self.datas['temperature'] = values['main']['temp']
            self.datas['pressure'] = values['main']['pressure']
            self.datas['humidity'] = values['main']['humidity']
            self.datas['description'] = values['weather'][0]['description']
            self.datas['name'] = values['name']+" - "+str(values['sys']['country'])

            iconid=values['weather'][0]['icon']
            self.datas['icon_url'] = OPENWEATHER_ICON_BEGIN + str(iconid) +OPENWEATHER_ICON_END
            
            self.datas['errors'] = ''
            return True
