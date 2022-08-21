from pythonGoogleSheets import *
from sense_hat import SenseHat
from datetime import datetime
import time 

print('\nGetting Measures\n')

# Variables
waitTime = 600
dataIndex = 0

while True:

        sense = SenseHat()
        sense.clear()

        # Capture Current Datetime
        now = datetime.now()

        # Datetime to String
        dateTime = now.strftime("%Y-%m-%d %H:%M:%S")
        date = dateTime[:10]
        hour = dateTime[-8:]


        humidity = sense.get_humidity()
        temperature_from_humidity = sense.get_temperature()
        pressure = sense.get_pressure()
        temperature_from_pressure = sense.get_temperature_from_pressure()
        
        row = [ dataIndex, 
                dateTime, 
		date, 
		hour, 
		humidity, 
		temperature_from_humidity, 
		pressure, 
		temperature_from_pressure ]
        index = 2
        sheet.insert_row(row, index)   
        
        dataIndex += 1

        # Sleep time
        time.sleep(waitTime)