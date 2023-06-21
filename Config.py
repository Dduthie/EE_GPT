import configparser

class Configurator:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.settingsDict = {}
        self.settingsDict['width'] = int(self.config['USER']['screenWidth'])
        self.settingsDict['height'] = int(self.config['USER']['screenHeight'])
        self.settingsDict['icon'] = self.config['USER']['iconColour']
        self.settingsDict['theme'] = self.config['USER']['theme']
        
    def getDefaultView(self):
        width = self.config['DEFAULT']['screenWidth']
        height = self.config['DEFAULT']['screenHeight']
        return width, height
    
    def getDefaultIcon(self):
        return self.config['DEFAULT']['iconColour']
    
    def getDefaultTheme(self):
        return self.config['DEFAULT']['theme']
    
    def setUserSettings(self,settingsDict):
        self.config['USER']['screenWidth'] = settingsDict['width']
        self.config['USER']['screenHeight'] = settingsDict['height']
        self.config['USER']['iconColour'] = settingsDict['icon']
        self.config['USER']['theme'] = settingsDict['theme']
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)