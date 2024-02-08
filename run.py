import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pandas as pd

# Defining the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Use the credentials file to authorize the application
CREDS = Credentials.from_service_account_file('credits.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
client = gspread.authorize(SCOPED_CREDS)

# Accessing the Google Sheets
food = client.open("goodfood")

print("Welcome to your food tracker!")