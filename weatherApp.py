import sys
import requests
import json
from datetime import datetime

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap

from weather_window import Ui_MainWindow

locDisplay = ""
locUrl = ""
unitTemp = "C"
unitWind = "kmh"
apiKey = "1def0c78689f22035176fc71c68b106c"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tabHub.setCurrentIndex(0)

        self.loc_button_search.clicked.connect(self.loc_input)
        self.loc_button_OK.clicked.connect(self.loc_validation)
    
    def loc_input(self):
        """ Get the location input from user
        and send it to loc_output. 
        Link to button 'Search' """

        loc = self.loc_lineEdit.text()
        
        self.loc_output(loc)

    def loc_output(self, loc):
        """ Fill the comboBox.
        This function uses an API functionality to list city namesakes """ 

        self.loc_combo.clear()

        loc = loc.strip()
        loc = loc.title()
        #print(loc)

        url = f"http://api.openweathermap.org/geo/1.0/direct?q={loc}&limit=5&appid={apiKey}"

        response = requests.get(url)
        data = json.loads(response.text)
        code = response.status_code
        print(code)
        #print(data)

        if code != 200 or len(data) == 0:
            self.main_label_status.setText("NO MATCH")
            return None

        items = []
        for local in data:
            try:
                items.append(f"{local['name']}, {local['state'].lower()}, {local['country'].lower()}")
            except KeyError:
                items.append(f"{local['name']}, {local['country'].lower()}")

        #print(items)
        self.loc_combo.addItems(items)
    
    def loc_validation(self):
        global locDisplay, locUrl

        loc = self.loc_combo.currentText()
        locDisplay = loc

        loc = loc.split(",")
        #print(len(loc))
        #print(loc)

        """ if len(loc) < 2 :
            self.main_label_status.setText("NO MATCH")
            return None """

        if len(loc) == 3 :
            name = loc[0].replace(" ","+")
            #print(name)

            state = loc[1].strip()
            #print(state)

            country = loc[2].strip()
            #print(country)

            loc = [name, state, country]
            loc = ",".join(loc)
            locUrl = loc
            #print(locUrl)
        
        if len(loc) == 2 :
            name = loc[0].replace(" ","+")
            #print(name)

            country = loc[1].strip()
            #print(country)

            loc = [name, country]
            loc = ",".join(loc)
            locUrl = loc
            #print(locUrl)
        
        self.currentWeather()
        self.tabHub.setCurrentIndex(1)
    
    def tempConv(self, temp):
        if unitTemp == "K":
            return f"{round(temp)}K"

        elif unitTemp == "C":
            return f"{round(temp - 273.15)}°C"

        else :
            # (1 K − 273,15) × 9/5 + 32 = -457,9 °F
            F = (temp - 273.15) * 9/5 + 32
            return f"{round(F)}F"
    
    def windConv(self, wind):
        if unitWind == "ms":
            return f"{round(wind)} m/s"
        
        elif unitWind == "kmh":
            return f"{round(wind * 3.6)} km/h"
        
        else:
            # ms 2,237
            return f"{round(wind * 2.237)} m/s"
    
    def getIcon(self, id):
        icon = QImage()
        iconUrl = f"http://openweathermap.org/img/wn/{id}@2x.png"
        icon.loadFromData(requests.get(iconUrl).content)

        return QPixmap(icon)
    
    def currentWeather(self):

        # - - - - Get json
        url = f"https://api.openweathermap.org/data/2.5/weather?q={locUrl}&appid={apiKey}"
        response = requests.get(url)
        data = response.json()
        data = json.loads(response.text)

        # - - - - Current time
        today = datetime.now()
        date = today.strftime("%d/%m/%Y")
        hour = today.strftime("%H:%M")
        self.curr_label_recap.setText(f"{locDisplay} - {date} {hour}")


        # - - - - Temp frame
        # Current temp
        temp = data['main']['temp']
        #temp = round(temp - 273.15)
        self.curr_label_temp.setText(f"{self.tempConv(temp)}")

        # Weather description
        descr = data['weather'][0]['description']
        self.curr_label_temp_description.setText(descr)

        # Temp max/min/feels
        tempMax = self.tempConv(data['main']['temp_max'])
        tempMin = self.tempConv(data['main']['temp_min'])
        tempFeels = self.tempConv(data['main']['feels_like'])

        self.curr_label_temp_more.setText(
            f"Temp max : {tempMax}\nTemp min : {tempMin}\nFeels like : {tempFeels}")
        
        # Icon
        iconID = data['weather'][0]['icon']
        self.curr_icon_temp.setPixmap(self.getIcon(iconID))
    
    
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())