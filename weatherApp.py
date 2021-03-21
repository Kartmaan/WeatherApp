import sys
import requests
import socket
import json
from datetime import datetime
import time
import threading
import pickle

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap

from weather_window import Ui_MainWindow

__version__ = "1.0"
__author__ = "Kartmaan"

apiDefault = "1def0c78689f22035176fc71c68b106c"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.apiKey = apiDefault

		self.cityName = ""
		self.locDisplay = ""
		self.locUrl = ""
		self.lat = ""
		self.lon = ""

		self.unitTemp = "C" # Values : "C", "F", "K"
		self.unitWind = "kmh" # Values : "kmh", "ms", "mph"
		
		self.refreshRun = False # Weather refreshing
		self.t_init = 20*60 # Refresh interval (min)
		
		self.appRun = True
		self.connectionLost = False

		# - - - - Threads
		# Connection check
		self.thd_connectCheck = threading.Thread(target=self.checkConnection)
		self.thd_connectCheck.start()

		# Localisation validation
		self.thd_locValidation = threading.Thread(target=self.loc_validation)

		# Get the weather without refresh (just once)
		self.thd_weather = threading.Thread(target=self.getWeather)

		# Updates the weather at regular time intervals
		self.thd_refresh = threading.Thread(target=self.refresh)

		# Displaying Status Messages
		self.thd_status = threading.Thread(target=self.statusDisplay)

		# - - - - Connection of buttons with their function
		self.loc_button_search.clicked.connect(self.loc_output)
		self.loc_button_OK.clicked.connect(self.buttonOK)
		self.opt_button_saveAll.clicked.connect(self.saveAll)
		self.opt_button_verify.clicked.connect(self.verify)

		# - - - - Widgets initialisation
		self.tabHub.setCurrentIndex(0) # Display 1st tab first
		self.loc_button_OK.setEnabled(False) # Button OK off
		self.tab_current.setEnabled(False) # Current weather off
		self.tab_forecast.setEnabled(False) # Forecast off

		self.loadSave()

	def loc_output(self):
		""" Get location input and fill the comboBox.
		This function runs when "search" button is pressed. """ 

		self.loc_combo.clear() # Clear the comboBox
		loc = self.loc_lineEdit.text() # Get input

		# Formating
		loc = loc.strip()
		loc = loc.title()

		# Input is empty
		if len(loc) - loc.count(' ') == 0:
			self.main_label_status.setText("Please insert a valid city name")
			return None

		# an API to list the names of homonymous towns
		url = f"http://api.openweathermap.org/geo/1.0/direct?q={loc}&limit=5&appid={self.apiKey}"

		response = requests.get(url)
		data = json.loads(response.text)
		code = response.status_code

		# URL check
		if code != 200 or len(data) == 0:
			self.main_label_status.setText("NO MATCH")
			self.loc_button_OK.setEnabled(False)
			return None
		else:
			self.main_label_status.setText("")

		# Filling the comboBox with city names found
		"""the output can have 2 different syntaxes depending 
		on the city entered :
		1st syntax : city_name, state, country
		2nd syntax : city_name, country
		We first try to catch the 1st syntax and we 
		except a KeyError to catch the 2nd one """
		items = [] # list containing the names of homonymous towns
		for local in data:
			try:
				items.append(f"{local['name']}, {local['state'].lower()}, {local['country'].lower()}")
			except KeyError:
				items.append(f"{local['name']}, {local['country'].lower()}")

		self.loc_combo.addItems(items) # Combobox filling
		self.loc_button_OK.setEnabled(True) # Button OK ON
	
	def buttonOK(self):
		"""Button OK behaviour"""

		self.thd_locValidation = threading.Thread(target=self.loc_validation)
		self.thd_locValidation.start() 

	def loc_validation(self):
		""" Connect to 'OK' button
		- Get the choice from comboBox 
		- Format it to respect the syntax of the API URL
		- Runs the weather requests """

		# If waiting for updating, the process stops
		self.refreshRun = False
		if self.thd_refresh.is_alive():
			self.thd_refresh.join()

		# Get the comboBox choice
		loc = self.loc_combo.currentText()
		self.locDisplay = loc

		# str fragmentation
		loc = loc.split(",")

		# Formating for API URL
		# If syntax : [city_name, state, country]
		if len(loc) == 3:
			cityName = loc[0]
			self.main_label_title.setText(f"WhatsTheWeather in {cityName}")

			name = loc[0].replace(" ","+")

			state = loc[1].strip()

			country = loc[2].strip()

			# City name for API URL syntax
			loc = [name, state, country]
			loc = ",".join(loc)
			self.locUrl = loc
		
		# Formating for API URL
		# If syntax : [city_name, country]
		if len(loc) == 2:
			cityName = loc[0]
			self.main_label_title.setText(f"WhatsTheWeather in {cityName}")

			name = loc[0].replace(" ","+")

			country = loc[1].strip()

			loc = [name, country]
			loc = ",".join(loc)
			self.locUrl = loc

		# Meteorological data acquisition, without refreshing
		self.thd_weather = threading.Thread(target = self.getWeather)
		self.thd_weather.start()

		# Status message display
		self.thd_status = threading.Thread(target= self.statusDisplay, args=("get",))
		self.thd_status.start()

		# Acquisition of meteorological data, with refreshing
		self.refreshRun = True
		self.thd_weather.join()
		self.thd_refresh = threading.Thread(target=self.refresh)
		self.thd_refresh.start()

		# Enabling weather tabs
		self.tab_current.setEnabled(True)
		self.tab_forecast.setEnabled(True)
	
	def tempConv(self, temp):
		""" Temperature unit converter
		API unit (input) : Kelvin ("K") """

		if self.unitTemp == "K":
			return f"{round(temp)}K"

		elif self.unitTemp == "C":
			return f"{round(temp - 273.15)}°C"

		else: # unitTemp == "F"
			F = (temp - 273.15) * 9/5 + 32
			return f"{round(F)}F"
	
	def windConv(self, wind):
		""" Wind speed unit converter
		API unit (input) : m/s ("ms") """

		if self.unitWind == "ms":
			return f"{round(wind)} m/s"
		
		elif self.unitWind == "kmh":
			return f"{round(wind * 3.6)} km/h"
		
		else: # unitWind == "mph":
			return f"{round(wind * 2.237)} mph"
	
	def beaufort(self, wind):
		""" Convert wind speed (m/s) to a Beaufort scale value """

		if wind < 0.5:
			number = 0
			descr = "Calm"

		elif wind >= 0.5 and wind <= 1.5:
			number = 1
			descr = "Light air"

		elif wind >= 1.6 and wind <= 3.3:
			number = 2
			descr = "Light breeze"

		elif wind >= 3.4 and wind <= 5.5:
			number = 3
			descr = "Gentle breeze"
		
		elif wind >= 5.6 and wind <= 7.9:
			number = 4
			descr = "Moderate breeze"
		
		elif wind >= 8 and wind <= 10.7:
			number = 5
			descr = "Fresh breeze"
		
		elif wind >= 10.8 and wind <= 13.8:
			number = 6
			descr = "Strong breeze"
		
		elif wind >= 13.9 and wind <= 17.1:
			number = 7
			descr = "High wind"
		
		elif wind >= 17.2 and wind <= 20.7:
			number = 8
			descr = "Gale"
		
		elif wind >= 20.8 and wind <= 24.4:
			number = 9
			descr = "Strong gale"
		
		elif wind >= 24.5 and wind <= 28.4:
			number = 10
			descr = "Storm"
		
		elif wind >= 28.5 and wind <= 32.6:
			number = 11
			descr = "Violent storm"
		
		elif wind >= 32.7:
			number = 12
			descr = "Hurricane"
		
		else :
			number = "Error"
			descr = "Error"
		
		return number, descr

	def cardinal(self, deg):
		""" Convert an angle (degree) to a cardinal point """

		if (deg >= 0 and deg <= 22) or (deg >= 338 and deg <= 360):
			card = "North"

		elif deg > 22 and deg <= 67:
			card = "North-east"

		elif deg > 67 and deg <= 112:
			card = "East"

		elif deg > 112 and deg <= 157:
			card = "South-east"

		elif deg > 157 and deg <= 203:
			card = "South"

		elif deg > 203 and deg <= 247:
			card = "South-West"

		elif deg > 247 and deg <= 292:
			card = "West"

		elif deg > 292 and deg <= 337:
			card = "North-west"

		else :
			card = "ERROR"

		return card

	def getIcon(self, id):
		""" Display weather icon from an icon ID  """

		icon = QImage()
		iconUrl = f"http://openweathermap.org/img/wn/{id}@2x.png"
		icon.loadFromData(requests.get(iconUrl).content)

		return QPixmap(icon)
	
	def epochConv(self, epoch, mode = "hr"):
		""" Convert an Unix epoch to a date  """

		if mode == "hr": # Only display hour
			out = datetime.fromtimestamp(epoch)
			out = out.strftime("%H:%M")

		if mode == "dt": # Only display date
			out = datetime.fromtimestamp(epoch)
			out = out.strftime("%d/%m/%Y")
		
		if mode == "day": # Only display week day
			out = datetime.fromtimestamp(epoch)
			out = out.weekday()

			if out == 0:
				out = "Monday"
			if out == 1:
				out = "Tuesday"
			if out == 2:
				out = "Wednesday"
			if out == 3:
				out = "Thursday"
			if out == 4:
				out = "Friday"
			if out == 5:
				out = "Saturday"
			if out == 6:
				out = "Sunday"
		
		if mode == "all": # Display all
			out = datetime.fromtimestamp(epoch)
			out = out.strftime("%d/%m/%Y-%H:%M")
		
		return out

	def currentWeather(self):
		""" Acquisition of current meteorological data 
		and widgets updating """

		# - - - - Get json
		url = f"https://api.openweathermap.org/data/2.5/weather?q={self.locUrl}&appid={self.apiKey}"
		response = requests.get(url)
		code = response.status_code

		if code != 200:
			self.main_label_status.setText("Wrong API key")
			return None
		else:
			pass

		data = response.json()
		data = json.loads(response.text)

		# - - - - - - - - Current time - - - - - - - -
		# API time, not system time
		epoch = data['dt']
		tz = data['timezone']
		date = datetime.fromtimestamp(epoch)
		dt = date.strftime("%d/%m/%Y")
		hr = date.strftime("%H:%M")

		hrlt = epoch + tz - 3600
		hrlt = datetime.fromtimestamp(hrlt)
		hrlt = hrlt.strftime("%H:%M")

		self.curr_label_recap.setText(f"{self.locDisplay} - {dt} {hr} (local time : {hrlt})")

		# - - - - - - - - Temp frame - - - - - - - -
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

		# - - - - - - - - Wind frame - - - - - - - -
		wind = self.windConv(data['wind']['speed'])
		self.curr_label_wind_speed.setText(wind)
		
		# Beaufort scale
		bs = self.beaufort(round(data['wind']['speed'],1))
		text = f"Beaufort scale : {str(bs[0])}/12\n{str(bs[1])}"
		self.curr_label_wind_more.setText(text)

		# Degree/cardinal
		deg = data['wind']['deg']
		card = self.cardinal(deg)
		self.curr_label_wind_dir.setText(str(deg)+"°")
		self.curr_label_wind_cardinal.setText(card)

		# - - - - - - - - More info frame - - - - - - - -
		# Press\Vis\Hum
		press = data['main']['pressure']
		vis = data['visibility']
		hum = data['main']['humidity']
		text = f"Pressure : {press} hPa\n\nVisibility : {vis} m\n\nHumidity : {hum}%"
		self.curr_label_more_info_press.setText(text)

		# Sunrise/Sunset
		# To-Do : time zone 
		sunrise = data['sys']['sunrise'] + tz - 3600
		#print(sunrise)
		#print(data['timezone'])
		sunrise = datetime.fromtimestamp(sunrise)
		sunrise = sunrise.strftime("%H:%M")

		sunset = data['sys']['sunset'] + tz - 3600
		sunset = datetime.fromtimestamp(sunset)
		sunset = sunset.strftime("%H:%M")

		text = f"Sunrise : {sunrise}\n\nSunset : {sunset}"
		self.curr_label_sun.setText(text)

		# - - - - - - - - Next hours frame - - - - - - - -
		# To-Do : If the icon ID is the same as the previous hour, 
		# there is no need to request the API
		self.lat = data['coord']['lat']
		self.lon = data['coord']['lon']
		url = f"https://api.openweathermap.org/data/2.5/onecall?lat={self.lat}&lon={self.lon}&exclude=minutely,daily&appid={self.apiKey}"
		response = requests.get(url)
		data = json.loads(response.text)

		# - - - H+1
		hr = self.epochConv(data['hourly'][1]['dt'])
		iconID = data['hourly'][1]['weather'][0]['icon']
		temp = self.tempConv(data['hourly'][1]['temp'])
		wind = self.windConv(data['hourly'][1]['wind_speed'])

		self.curr_label_h1.setText(hr)
		self.curr_icon_h1.setPixmap(self.getIcon(iconID))
		self.curr_label_h1_info.setText(f"{temp}\n{wind}")

		# - - - H+2
		hr = self.epochConv(data['hourly'][2]['dt'])
		iconID = data['hourly'][2]['weather'][0]['icon']
		temp = self.tempConv(data['hourly'][2]['temp'])
		wind = self.windConv(data['hourly'][2]['wind_speed'])

		self.curr_label_h2.setText(hr)
		self.curr_icon_h2.setPixmap(self.getIcon(iconID))
		self.curr_label_h2_info.setText(f"{temp}\n{wind}")

		# - - - H+3
		hr = self.epochConv(data['hourly'][3]['dt'])
		iconID = data['hourly'][3]['weather'][0]['icon']
		temp = self.tempConv(data['hourly'][3]['temp'])
		wind = self.windConv(data['hourly'][3]['wind_speed'])

		self.curr_label_h3.setText(hr)
		self.curr_icon_h3.setPixmap(self.getIcon(iconID))
		self.curr_label_h3_info.setText(f"{temp}\n{wind}")

		# - - - H+4
		hr = self.epochConv(data['hourly'][4]['dt'])
		iconID = data['hourly'][4]['weather'][0]['icon']
		temp = self.tempConv(data['hourly'][4]['temp'])
		wind = self.windConv(data['hourly'][4]['wind_speed'])

		self.curr_label_h4.setText(hr)
		self.curr_icon_h4.setPixmap(self.getIcon(iconID))
		self.curr_label_h4_info.setText(f"{temp}\n{wind}")

		# - - - H+5
		hr = self.epochConv(data['hourly'][5]['dt'])
		iconID = data['hourly'][5]['weather'][0]['icon']
		temp = self.tempConv(data['hourly'][5]['temp'])
		wind = self.windConv(data['hourly'][5]['wind_speed'])

		self.curr_label_h5.setText(hr)
		self.curr_icon_h5.setPixmap(self.getIcon(iconID))
		self.curr_label_h5_info.setText(f"{temp}\n{wind}")

		# - - - H+6
		hr = self.epochConv(data['hourly'][6]['dt'])
		iconID = data['hourly'][6]['weather'][0]['icon']
		temp = self.tempConv(data['hourly'][6]['temp'])
		wind = self.windConv(data['hourly'][6]['wind_speed'])

		self.curr_label_h6.setText(hr)
		self.curr_icon_h6.setPixmap(self.getIcon(iconID))
		self.curr_label_h6_info.setText(f"{temp}\n{wind}")       

	def forecastWeather(self):
		""" Acquisition of forecast meteorological data 
		and widgets updating """

		url = f"https://api.openweathermap.org/data/2.5/onecall?lat={self.lat}&lon={self.lon}&exclude=minutely,hourly&appid={self.apiKey}"
		response = requests.get(url)
		code = response.status_code

		if code != 200:
			self.main_label_status.setText("Wrong API key")
			return None
		else:
			pass

		data = json.loads(response.text)

		# - - - Today
		tempMin = self.tempConv(data['daily'][0]['temp']['min'])
		tempMax = self.tempConv(data['daily'][0]['temp']['max'])
		iconID = data['daily'][0]['weather'][0]['icon']
		descr = data['daily'][0]['weather'][0]['description']

		self.for_label_today_minTemp.setText(tempMin)
		self.for_label_today_maxTemp.setText(tempMax)
		self.for_label_today_descr.setText(descr)
		self.for_icon_today.setPixmap(self.getIcon(iconID))

		# - - - Day +1
		day = self.epochConv(data['daily'][1]['dt'], "day")
		tempMin = self.tempConv(data['daily'][1]['temp']['min'])
		tempMax = self.tempConv(data['daily'][1]['temp']['max'])
		iconID = data['daily'][1]['weather'][0]['icon']
		descr = data['daily'][1]['weather'][0]['description']

		self.for_label_d1.setText(day)
		self.for_label_d1_minTemp.setText(tempMin)
		self.for_label_d1_maxTemp.setText(tempMax)
		self.for_label_d1_descr.setText(descr)
		self.for_icon_d1.setPixmap(self.getIcon(iconID))

		# - - - Day +2
		day = self.epochConv(data['daily'][2]['dt'], "day")
		tempMin = self.tempConv(data['daily'][2]['temp']['min'])
		tempMax = self.tempConv(data['daily'][2]['temp']['max'])
		iconID = data['daily'][2]['weather'][0]['icon']
		descr = data['daily'][2]['weather'][0]['description']

		self.for_label_d2.setText(day)
		self.for_label_d2_minTemp.setText(tempMin)
		self.for_label_d2_maxTemp.setText(tempMax)
		self.for_label_d2_descr.setText(descr)
		self.for_icon_d2.setPixmap(self.getIcon(iconID))

		# - - - Day +3
		day = self.epochConv(data['daily'][3]['dt'], "day")
		tempMin = self.tempConv(data['daily'][3]['temp']['min'])
		tempMax = self.tempConv(data['daily'][3]['temp']['max'])
		iconID = data['daily'][3]['weather'][0]['icon']
		descr = data['daily'][3]['weather'][0]['description']

		self.for_label_d3.setText(day)
		self.for_label_d3_minTemp.setText(tempMin)
		self.for_label_d3_maxTemp.setText(tempMax)
		self.for_label_d3_descr.setText(descr)
		self.for_icon_d3.setPixmap(self.getIcon(iconID))

		# - - - Day +4
		day = self.epochConv(data['daily'][4]['dt'], "day")
		tempMin = self.tempConv(data['daily'][4]['temp']['min'])
		tempMax = self.tempConv(data['daily'][4]['temp']['max'])
		iconID = data['daily'][4]['weather'][0]['icon']
		descr = data['daily'][4]['weather'][0]['description']

		self.for_label_d4.setText(day)
		self.for_label_d4_minTemp.setText(tempMin)
		self.for_label_d4_maxTemp.setText(tempMax)
		self.for_label_d4_descr.setText(descr)
		self.for_icon_d4.setPixmap(self.getIcon(iconID))

		# - - - Day +5
		day = self.epochConv(data['daily'][5]['dt'], "day")
		tempMin = self.tempConv(data['daily'][5]['temp']['min'])
		tempMax = self.tempConv(data['daily'][5]['temp']['max'])
		iconID = data['daily'][5]['weather'][0]['icon']
		descr = data['daily'][5]['weather'][0]['description']

		self.for_label_d5.setText(day)
		self.for_label_d5_minTemp.setText(tempMin)
		self.for_label_d5_maxTemp.setText(tempMax)
		self.for_label_d5_descr.setText(descr)
		self.for_icon_d5.setPixmap(self.getIcon(iconID))

		# - - - Day +6
		day = self.epochConv(data['daily'][6]['dt'], "day")
		tempMin = self.tempConv(data['daily'][6]['temp']['min'])
		tempMax = self.tempConv(data['daily'][6]['temp']['max'])
		iconID = data['daily'][6]['weather'][0]['icon']
		descr = data['daily'][6]['weather'][0]['description']

		self.for_label_d6.setText(day)
		self.for_label_d6_minTemp.setText(tempMin)
		self.for_label_d6_maxTemp.setText(tempMax)
		self.for_label_d6_descr.setText(descr)
		self.for_icon_d6.setPixmap(self.getIcon(iconID))

		# - - - Day +7
		day = self.epochConv(data['daily'][7]['dt'], "day")
		tempMin = self.tempConv(data['daily'][7]['temp']['min'])
		tempMax = self.tempConv(data['daily'][7]['temp']['max'])
		iconID = data['daily'][7]['weather'][0]['icon']
		descr = data['daily'][7]['weather'][0]['description']

		self.for_label_d7.setText(day)
		self.for_label_d7_minTemp.setText(tempMin)
		self.for_label_d7_maxTemp.setText(tempMax)
		self.for_label_d7_descr.setText(descr)
		self.for_icon_d7.setPixmap(self.getIcon(iconID))

	def verify(self, mode = 1):
		""" Checking API validity
		Connect to 'verify' button """

		inputApi = self.opt_lineEdit_api.text()
		url = f"https://api.openweathermap.org/data/2.5/weather?q=Lyon&appid={inputApi}"
		response = requests.get(url)
		code = response.status_code
		
		if code == 200:
			self.apiKey = inputApi
			if mode == 1:
				self.main_label_status.setText("API OK")
			if mode == 2:
				#self.main_label_status.setText("API OK")
				return True
		else:
			apiKey = apiDefault
			self.opt_lineEdit_api.setText(apiKey)
			self.main_label_status.setText("Wrong API key, back to the default one")
			if mode == 2:
				return False

	def saveAll(self):
		""" Save user options, restart an API call 
		for the acquisition of meteorological data """

		self.refreshRun = False
		if self.thd_refresh.is_alive():
			self.refreshRun = False
			self.thd_refresh.join()

		if self.opt_radio_celcius.isChecked():
			self.unitTemp = "C"
		if self.opt_radio_farh.isChecked():
			self.unitTemp = "F"
		if self.opt_radio_kelvin.isChecked():
			self.unitTemp = "K"
		
		if self.opt_radio_kmh.isChecked():
			self.unitWind = "kmh"
		if self.opt_radio_ms.isChecked():
			self.unitWind = "ms"
		if self.opt_radio_mph.isChecked():
			self.unitWind = "mph"
		
		self.apiKey = self.opt_lineEdit_api.text()
		self.verify(mode = 2)

		self.t_init = self.opt_spinBox_refresh.value() * 60

		self.storeSave()

		self.thd_status = threading.Thread(target=self.statusDisplay, args=("save",))
		self.thd_status.start()

		if self.locUrl != "":
			self.thd_weather = threading.Thread(target=self.getWeather)
			self.thd_weather.start()

			self.refreshRun = True
			self.thd_refresh = threading.Thread(target=self.refresh)
			self.thd_refresh.start()

	def checkConnection(self, host="8.8.8.8", port=53, timeout=3):
		#global refreshRun
		backOnline = False

		while self.appRun:
			try: # Connection OK
				socket.setdefaulttimeout(timeout)
				socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

				if backOnline: # Connection reestablished after an outage
					self.connectionLost = False
					self.main_label_status.setText("Back online")
					self.loc_button_OK.setEnabled(True)
					self.opt_button_saveAll.setEnabled(True)
					self.opt_button_verify.setEnabled(True)

					#self.thd_refresh.start()

					backOnline = False

				""" if refreshRun == False:
					refreshRun == True """

			except socket.error as ex: # Connection lost
				print(ex)
				""" if self.thd_refresh.is_alive():
					refreshRun = False
					self.thd_refresh.join() """

				self.connectionLost = True

				self.loc_button_OK.setEnabled(False)
				self.opt_button_saveAll.setEnabled(False)
				self.opt_button_verify.setEnabled(False)

				self.main_label_status.setText("NO CONNECTION")
				backOnline = True
			
			t = 9
			while t > 0 and self.appRun:
				time.sleep(1)
				t -= 1

	def storeSave(self):
		# To-do : New API keys saving in .txt file
		apiKey = self.apiKey
		temp = self.unitTemp
		wind = self.unitWind
		timer = self.opt_spinBox_refresh.value()

		save = {"apiKey" : apiKey, "temp" : temp, "wind" : wind, "timer" : timer}

		svFile = open('saveFile', 'wb')

		pickle.dump(save, svFile)
		svFile.close()
	
	def loadSave(self):
		try :
			svFile = open('saveFile', 'rb')
			save = pickle.load(svFile)
			svFile.close()

			self.apiKey = save['apiKey']
			self.opt_lineEdit_api.setText(save['apiKey'])

			self.unitTemp = save['temp']
			if save['temp'] == "C":
				self.opt_radio_celcius.setChecked(True)
			if save['temp'] == "F":
				self.opt_radio_farh.setChecked(True)
			if save['temp'] == "K":
				self.opt_radio_kelvin.setChecked(True)

			self.unitWind = save['wind']
			if save['wind'] == "kmh":
				self.opt_radio_kmh.setChecked(True)
			if save['wind'] == "ms":
				self.opt_radio_ms.setChecked(True)
			if save['wind'] == "mph":
				self.opt_radio_mph.setChecked(True)

			self.t_init = save['timer'] * 60
			self.opt_spinBox_refresh.setValue(save['timer'])

		except FileNotFoundError:
			self.apiKey = apiDefault
			pass

	def refresh(self):
		"""Get the weather (current & forecast), with refresh"""
		
		t = self.t_init

		while self.refreshRun:
			while t and self.refreshRun:
				if self.refreshRun == False:
					break
				mins, secs = divmod(t, 60)
				timer = "Next refresh in : {:02d}:{:02d}".format(mins, secs)
				self.opt_label_countDown.setText(timer)

				""" If the connection is lost, the countdown pauses until 
				the connection is back. """
				if self.connectionLost:
					while True:
						time.sleep(0.5)
						if self.connectionLost == False:
							break

				time.sleep(1)
				t -= 1

			if self.refreshRun:
				self.currentWeather()
				self.tabHub.setCurrentIndex(1)
				self.forecastWeather()
				
			t = self.t_init
	
	def getWeather(self):
		"""Get the weather just once (curren & forecast), 
		without refresh"""

		self.thd_status = threading.Thread(target= self.statusDisplay, args=("get",))
		self.thd_status.start()

		self.currentWeather()
		self.forecastWeather()
		self.tabHub.setCurrentIndex(1)

	def statusDisplay(self, flag):
		"""Status messages display"""

		t = 3 # Display time (sec)
		
		if flag == "save":
			txt = "Preferences have been saved"
		if flag == "noMatch":
			txt = "NO MATCH - Please retry"
		if flag == "get":
			txt = "Getting. . ."
		
		self.main_label_status.setText(txt)
		time.sleep(t)
		self.main_label_status.setText("")

	def closeEvent(self, event):
		""" App closure stops the refresh process """

		event.accept()
		self.refreshRun = False
		self.appRun = False
		if self.thd_refresh.is_alive():
			self.thd_refresh.join()

		if self.thd_connectCheck.is_alive():
			self.thd_connectCheck.join()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	main_window = MainWindow()
	main_window.show()
	sys.exit(app.exec_())