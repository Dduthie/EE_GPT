import configparser
from ast import literal_eval

class Configurator:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.settingsDict = {}
        for key, value in self.config['USER'].items():
            try:
                self.settingsDict[key] = literal_eval(value)
            except ValueError: 
                self.settingsDict[key] = value

    def getDefaultView(self):
        width = self.config['DEFAULT']['screenwidth']
        height = self.config['DEFAULT']['screenheight']
        return width, height

    def getDefaultIcon(self):
        return self.config['DEFAULT']['iconcolour']

    def getDefaultTheme(self):
        return self.config['DEFAULT']['theme']

    def setUserSettings(self,settingsDict:dict):
        for key, value in settingsDict.items():
            self.config['USER'][key] = value
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)