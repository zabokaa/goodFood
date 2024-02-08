import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Defining the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Use the credentials file to authorize the application
CREDITS = Credentials.from_service_account_file('credits.json')
SCOPED_CREDS = CREDITS.with_scopes(SCOPE)
client = gspread.authorize(SCOPED_CREDS)

# Accessing the Google Sheets
goodfood = client.open("goodfood")

print("Welcome to your food tracker GOOD FOOD!")

def add_food_entry():
    """
    Add a new food entry to the food tracker
    """
    food = input("Please enter the type of food you ate: \n")
    feeling = input("How did you feel after eating the food? Please enter a number between 1=feeling good and 5= bad feeling: \n")
    date = datetime.now().strftime("%d/%m/%Y\n")

     # Create a new row of data + append to spreadsheet
    new_row = [food, feeling, date]
    goodfood.sheet1.append_row(new_row)

    print(f"You added {food} to the food tracker with a value of {feeling} on {date}.")

# CALL THE FUNCTION !!
add_food_entry()