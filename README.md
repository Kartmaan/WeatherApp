# WeatherApp
A PyQt5 graphical weather application using OpenWeatherMap API, the program retrieves weather data and updates it regularly

## What does the program do ? :
- Finds the city name entered by the user as well as its namesakes

- Displays current weather data for the location :
  - Current temperature with a description and an icon
  - Feels like temperature
  - Max/min temperature
  - Wind speed
  - Wind direction (degree and cardinal)
  - Wind score and description in Beaufort scale
  - Pressure (hP)
  - Visibility (km)
  - Humidity
  - Sunrise/sunset time
  - Next hours weather (6h) with hours, icons, temperatures and wind speeds
  
- Displays forecast weather data for the location (7 days). For each day :
  - Week day
  - Min/max temperature
  - Weather description
  - Weather icon
  
- User can change some options
  - Use their own API key (OpenWeatherMap API)
  - Change the temperature unit
    - Celcius
    - Fahrenheit
    - Kelvin
  - Change the wind speed unit
    - km/h
    - m/s
    - mph
  - Change the refresh timer

- The program periodically checks the status of the Internet connection, if it goes down, some buttons are deactivated and the refresh countdown is paused until a connection is found.
- User preferences are saved in a binary file which will be loaded each time the application is started
- The local time is displayed in brackets for each city name chosen
- A countdown is displayed in the option tab allowing to know when the next refresh will take place
- A 'verify' button is used to verify the validity of an API key before saving the parameters
- A rectangular zone at the bottom of the window is used to display the status messages
