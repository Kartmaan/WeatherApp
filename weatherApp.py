import sys
import requests
import json
from datetime import datetime
import time
import threading

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap

from weather_window import Ui_MainWindow

__version__ = "1.0"
__author__ = "Kartmaan"

run = False
t_init = 20*60
cityName = ""
locDisplay = ""
locUrl = ""
lat = ""
lon = ""
unitTemp = "C" # "C", "F", "K"
unitWind = "kmh" # "kmh", "ms", "mph"
apiDefault = "1def0c78689f22035176fc71c68b106c"
apiKey = "1def0c78689f22035176fc71c68b106c"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.thd_refresh = threading.Thread(target=self.refresh)
		self.thd_status = threading.Thread(target=self.statusDisplay)
		self.thd_weather = threading.Thread(target=self.getWeather)
		self.thd_locValidation = threading.Thread(target=self.loc_validation)

		self.tabHub.setCurrentIndex(0)
		self.loc_button_OK.setEnabled(False)
		self.tab_current.setEnabled(False)
		self.tab_forecast.setEnabled(False)

		self.loc_button_search.clicked.connect(self.loc_output)
		self.loc_button_OK.clicked.connect(self.buttonOK)
		self.opt_button_saveAll.clicked.connect(self.saveAll)
		self.opt_button_verify.clicked.connect(self.verify)
	
	def loc_output(self):
		""" Fill the comboBox.
		This function uses an API functionality to list city namesakes """ 

		loc = self.loc_lineEdit.text()
		loc = loc.strip()
		loc = loc.title()

		if len(loc) - loc.count(' ') == 0:
			self.main_label_status.setText("Please insert a valid city name")
			return None

		self.loc_combo.clear()

		url = f"http://api.openweathermap.org/geo/1.0/direct?q={loc}&limit=5&appid={apiKey}"

		response = requests.get(url)
		data = json.loads(response.text)
		code = response.status_code
		print(code)
		#print(data)

		if code != 200 or len(data) == 0:
			self.main_label_status.setText("NO MATCH")
			self.loc_button_OK.setEnabled(False)
			return None
		else:
			self.main_label_status.setText("")

		items = []
		for local in data:
			try:
				items.append(f"{local['name']}, {local['state'].lower()}, {local['country'].lower()}")
			except KeyError:
				items.append(f"{local['name']}, {local['country'].lower()}")

		#print(items)
		self.loc_combo.addItems(items)
		self.loc_button_OK.setEnabled(True)
	
	def buttonOK(self):
		self.thd_locValidation = threading.Thread(target=self.loc_validation)
		self.thd_locValidation.start() 

	def loc_validation(self):
		global locDisplay, locUrl, cityName, run

		run = False
		if self.thd_refresh.is_alive():
			self.thd_refresh.join()

		loc = self.loc_combo.currentText()
		locDisplay = loc

		loc = loc.split(",")

		if len(loc) == 3:
			cityName = loc[0]
			self.main_label_title.setText(f"WhatsTheWeather in {cityName}")

			name = loc[0].replace(" ","+")

			state = loc[1].strip()

			country = loc[2].strip()

			loc = [name, state, country]
			loc = ",".join(loc)
			locUrl = loc
		
		if len(loc) == 2:
			cityName = loc[0]
			self.main_label_title.setText(f"WhatsTheWeather in {cityName}")

			name = loc[0].replace(" ","+")

			country = loc[1].strip()

			loc = [name, country]
			loc = ",".join(loc)
			locUrl = loc
		
		self.thd_weather = threading.Thread(target = self.getWeather)
		self.thd_weather.start()

		self.thd_status = threading.Thread(target= self.statusDisplay, args=("get",))
		self.thd_status.start()
		#self.status("Getting. . .")

		run = True
		self.thd_weather.join()
		self.thd_refresh = threading.Thread(target=self.refresh)
		self.thd_refresh.start()

		self.tab_current.setEnabled(True)
		self.tab_forecast.setEnabled(True)

		#self.tabHub.setCurrentIndex(1)
	
	def tempConv(self, temp):
		#global unitTemp

		if unitTemp == "K":
			return f"{round(temp)}K"

		elif unitTemp == "C":
			return f"{round(temp - 273.15)}°C"

		else: # unitTemp == "F" :
			# (1 K − 273,15) × 9/5 + 32 = -457,9 °F
			F = (temp - 273.15) * 9/5 + 32
			return f"{round(F)}F"
	
	def windConv(self, wind):
		#global unitWind

		if unitWind == "ms":
			return f"{round(wind)} m/s"
		
		elif unitWind == "kmh":
			return f"{round(wind * 3.6)} km/h"
		
		else: # unitWind == "mph":
			return f"{round(wind * 2.237)} mph"
	
	def beaufort(self, wind):
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
		icon = QImage()
		iconUrl = f"http://openweathermap.org/img/wn/{id}@2x.png"
		icon.loadFromData(requests.get(iconUrl).content)

		return QPixmap(icon)
	
	def epochConv(self, epoch, mode = "hr"):
		if mode == "hr":
			out = datetime.fromtimestamp(epoch)
			out = out.strftime("%H:%M")

		if mode == "dt":
			out = datetime.fromtimestamp(epoch)
			out = out.strftime("%d/%m/%Y")
		
		if mode == "day":
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
		
		if mode == "all":
			out = datetime.fromtimestamp(epoch)
			out = out.strftime("%d/%m/%Y-%H:%M")
		
		return out

	def currentWeather(self):

		global lat, lon

		#self.main_label_status.setText("Current weather data acquisition...")

		# - - - - Get json
		url = f"https://api.openweathermap.org/data/2.5/weather?q={locUrl}&appid={apiKey}"
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
		""" today = datetime.now()
		date = today.strftime("%d/%m/%Y")
		hour = today.strftime("%H:%M") """

		epoch = data['dt']
		tz = data['timezone']
		date = datetime.fromtimestamp(epoch)
		dt = date.strftime("%d/%m/%Y")
		hr = date.strftime("%H:%M")

		hrlt = epoch + tz - 3600
		hrlt = datetime.fromtimestamp(hrlt)
		hrlt = hrlt.strftime("%H:%M")

		self.curr_label_recap.setText(f"{locDisplay} - {dt} {hr} (local time : {hrlt})")


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
		lat = data['coord']['lat']
		lon = data['coord']['lon']
		url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,daily&appid={apiKey}"
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
		#self.main_label_status.setText("Forecast weather data acquisition...")

		url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={apiKey}"
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

	def verify(self):
		global apiKey, apiDefault

		inputApi = self.opt_lineEdit_api.text()
		url = f"https://api.openweathermap.org/data/2.5/weather?q=Lyon&appid={inputApi}"
		response = requests.get(url)
		code = response.status_code
		
		if code == 200:
			apiKey = inputApi
			self.main_label_status.setText("API OK")
		else:
			apiKey = apiDefault
			self.opt_lineEdit_api.setText(apiKey)
			self.main_label_status.setText("Wrong API key, back to the default one")

	def saveAll(self):
		global unitTemp, unitWind, apiKey, run, t_init

		run = False
		if self.thd_refresh.is_alive():
			run = False
			self.thd_refresh.join()

		if self.opt_radio_celcius.isChecked():
			unitTemp = "C"
		if self.opt_radio_farh.isChecked():
			unitTemp = "F"
		if self.opt_radio_kelvin.isChecked():
			unitTemp = "K"
		
		if self.opt_radio_kmh.isChecked():
			unitWind = "kmh"
		if self.opt_radio_ms.isChecked():
			unitWind = "ms"
		if self.opt_radio_mph.isChecked():
			unitWind = "mph"
		
		apiKey = self.opt_lineEdit_api.text()

		t_init = self.opt_spinBox_refresh.value() * 60

		self.thd_status = threading.Thread(target=self.statusDisplay, args=("save",))
		self.thd_status.start()

		if locUrl != "":
			""" self.currentWeather()
			self.forecastWeather()
			self.tabHub.setCurrentIndex(1) """
			self.thd_weather = threading.Thread(target=self.getWeather)
			self.thd_weather.start()

			run = True
			self.thd_refresh = threading.Thread(target=self.refresh)
			self.thd_refresh.start()
			
	def refresh(self):
		
		t = t_init
		
		self.currentWeather()
		self.forecastWeather()
		self.tabHub.setCurrentIndex(1)

		while run:
			while t and run:
				if run == False:
					break
				mins, secs = divmod(t, 60)
				timer = "Next refresh in : {:02d}:{:02d}".format(mins, secs)
				self.opt_label_countDown.setText(timer)
				time.sleep(1)
				t -= 1

			if run:
				self.currentWeather()
				self.tabHub.setCurrentIndex(1)
				self.forecastWeather()
				
			t = t_init
	
	def getWeather(self):
		"""Get the weather just once, without refresh"""

		self.thd_status = threading.Thread(target= self.statusDisplay, args=("get",))
		self.thd_status.start()
		#self.status("Getting. . .")

		self.currentWeather()
		self.forecastWeather()
		self.tabHub.setCurrentIndex(1)

	def statusDisplay(self, flag):
		t = 4
		
		if flag == "save":
			txt = "Preferences have been saved"
		if flag == "noMatch":
			txt = "NO MATCH - Please retry"
		if flag == "get":
			txt = "Getting. . ."
		
		self.main_label_status.setText(txt)
		time.sleep(t)
		self.main_label_status.setText("")

	def status(self, txt):
		if self.thd_status.is_alive():
			self.thd_status.join()
		
		self.thd_status = threading.Thread(target=self.statusDisplay, args=(txt,))

	def closeEvent(self, event):
		global run

		event.accept()
		run = False
		if self.thd_refresh.is_alive():
			self.thd_refresh.join()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	main_window = MainWindow()
	main_window.show()
	sys.exit(app.exec_())