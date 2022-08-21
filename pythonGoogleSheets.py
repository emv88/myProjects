
# Get API credentials and read them
keyAPI = 'mdrive.json'
googleFile = 'weatherStationLog'

import json 

with open(keyAPI) as f:
    data = json.load(f)

# Connect with the API

# conda install -c conda-forge oauth2client or pip install gspread oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('mdrive.json', scope)
client = gspread.authorize(creds)
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open(googleFile).sheet1
# Extract and print all of the values
data = sheet.get_all_records()


# Insert rows
#row = ['2:38pm', '60', '32', '960']
#index = 2
#sheet.insert_row(row, index)

# Video: https://youtu.be/3OnT1PfDrfE 
# Code: https://www.worthwebscraping.com/how-to-update-google-spreadsheet-using-python/


