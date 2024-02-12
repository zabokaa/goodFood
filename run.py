import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
# debugging error Heroku deployment
import os
import json

# Defining the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Use the credentials file to authorize the application

# debugging error Heroku deployment
creds_json = os.environ.get('CREDITS')
creds_dict = json.loads(creds_json)
CREDITS = Credentials.from_service_account_info(creds_dict)

# CREDITS = Credentials.from_service_account_file('credits.json')
SCOPED_CREDS = CREDITS.with_scopes(SCOPE)
client = gspread.authorize(SCOPED_CREDS)

# Accessing the Google Sheets
goodfood = client.open("goodfood")

print("Welcome to your food tracker GOOD FOOD!")

def menu():  
    """
    Menu for the programme
    """
    # Loop to keep the menu running
    while True:
        print( "\nWhat do you want to do? \n")  
        print( "1. Add a new food entry")  
        print( "2. See the average feeling of a type of food you ate")  
        print( "3. Delete one food entry")  
        print( "4. Search for food entries by date")
        print( "5. Exit")  
    # validation:
        while True:
                try:
                    menu_choice = int(input("Enter your choice: "))
                    if menu_choice > 0 and menu_choice < 6:
                        break
                    else:
                        print("You can only enter values from 1 to 5. Try again.\n")
                except ValueError:
                    print("You can only enter values from 1 to 5. Try again.\n")

        """
            Choose the function to run based on the user's choice and call it
        """
        if menu_choice == 1:  
            add_food_entry()
        elif menu_choice == 2:
            average_feeling()
        elif menu_choice == 3:
            delete_food_entry()
        elif menu_choice == 4:
            search_by_date()
        elif menu_choice == 5:
            print("Have a lovely day, eat good food and see you soon!")
            break

def add_food_entry():
    """
    Add a new food entry to the food tracker
    """
    food = input("Please enter the type of food you ate: \n")
    feeling = input("How did you feel after eating the food? Please enter a number between 1=feeling good and 5= bad feeling: \n")
    date = datetime.now().strftime("%d/%m/%Y")

     # Create a new row of data + append to spreadsheet
    new_row = [food, feeling, date]
    goodfood.sheet1.append_row(new_row)

    print(f"You added {food} to the food tracker with a value of {feeling} on {date}.")

def average_feeling():
    """
    Calculate the average feeling of a type of food
    """
    matching_rows = []
    food_type = input("Please enter the type of food you want to see the average feeling for: \n")
    rows = goodfood.sheet1.get_all_values()
    matching_rows = [row for row in rows if str(row[0]) == str(food_type)]
    # debug ZeroDivisionError:
    if len(matching_rows) > 0:
        average_feeling = sum(int(row[1]) for row in matching_rows) / len(matching_rows)
        print(f"The average feeling for {food_type} is {average_feeling}")
    else:
        print(f"No entries found for {food_type}")
    
def delete_food_entry():
    """
    Delete a food entry from the food tracker choose by name and date
    """
    food_type = input("Please enter the type of food you want to delete: \n")
    date = input("Please enter the date of the food entry you want to delete (dd/mm/yyyy): \n")
    rows = goodfood.sheet1.get_all_values()
    # iterating over a list and access indeces
    matching_rows = [i for i, row in enumerate(rows, start=1) if row[0] == food_type.strip() and row[2].strip() == date]

    if not matching_rows:
        print(f"No entries found for {food_type} on {date}")
        return

    # delete the chosen food entry, reversed to avoid index errors !
    for i in reversed(matching_rows):
        goodfood.sheet1.delete_rows(i, i)

    print(f"You deleted the entry/entries for {food_type} on {date}")

def search_by_date():
    """
    Search for food entries by date
    """
    print("You searched for food entries by date")

menu()
