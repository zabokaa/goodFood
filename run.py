import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from prettytable import PrettyTable
import os
import json

# Defining the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Use the credentials file to authorize the application

creds_json = os.environ.get('CREDITS')
creds_dict = json.loads(creds_json)
CREDITS = Credentials.from_service_account_info(creds_dict)
SCOPED_CREDS = CREDITS.with_scopes(SCOPE)
client = gspread.authorize(SCOPED_CREDS)

# Accessing the Google Sheets
goodfood = client.open("goodfood")

print("Welcome to your food tracker GOOD FOOD!")


def menu():
    """
    Menu for the programme
    """
    while True:
        print("\nWhat do you want to do? \n")
        print("Choose the according number between 1 and 5 \n")
        print("1. Add a new food entry")
        print("2. See the average feeling of a type of food you ate")
        print("3. Delete one food entry")
        print("4. Search for food entries by date")
        print("5. Exit")

        while True:
            try:
                menu_choice = int(input("Enter your choice: "))
                if menu_choice > 0 and menu_choice < 6:
                    break
                else:
                    print("You can only enter values from 1 to 5. "
                          "Try again.\n")
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
            print_with_frame("Have a lovely day, eat good food "
                             "and see you soon!")
            break


def add_food_entry():
    """
    Add a new food entry to the food tracker
    """
    while True:
        food = input("Please enter the type of food you ate: \n").capitalize()
        if food.isalpha():
            break
        else:
            print("You can only enter letters. Pls, try again.\n")

    while True:
        try:
            feeling = int(input("How did you feel after eating the food? "
                                "Please enter a number between 1=feeling good "
                                "and 5= feeling bad: \n"))
            if feeling > 0 and feeling < 6:
                break
            else:
                print("You can only enter values from 1 to 5. "
                      "Pls try again.\n")
        except ValueError:
            print("You can only enter values from 1 to 5. Pls try again.\n")
    date = datetime.now().strftime("%d/%m/%Y")
    new_row = [food, feeling, date]
    goodfood.sheet1.append_row(new_row)
    print_with_frame(f"You added {food} to the food tracker with a value "
                     f"of {feeling} on {date}.")


def average_feeling():
    """
    Calculate the average feeling of a type of food
    """
    matching_rows = []
    av_feeling = 0
    while True:
        food_type = input("Please enter the type of food you want to see "
                          "the average feeling for: \n").capitalize()
        if food_type.isalpha():
            break
        else:
            print("You can only enter letters. Pls, try again.\n")
    rows = goodfood.sheet1.get_all_values()
    matching_rows = [row for row in rows if str(row[0]) == str(food_type)]
    if len(matching_rows) > 0:
        av_feeling = (
            sum(int(row[1]) for row in matching_rows)
            / len(matching_rows)
        )
        print_with_frame(f"The average feeling for {food_type} "
                         f"is {av_feeling}")
    else:
        print(f"No entries found for {food_type}")


def delete_food_entry():
    """
    Delete a food entry from the food tracker choose by name and date
    """
    while True:
        food_type = input("Please enter the type of "
                          "food you want to delete: \n").capitalize()
        if food_type.isalpha():
            break
        else:
            print("You can only enter letters. Pls, try again.\n")
    rows = goodfood.sheet1.get_all_values()
    matching_rows = [
        (i, row) for i, row in enumerate(rows, start=1)
        if row[0] == food_type.strip() 
        ]
    if not matching_rows:
        print(f"No entries found for {food_type}")
        return
    print("Here are all the entries for this food type:")
    for selector, (i, row) in enumerate(matching_rows, start=1):
        print(f"{selector}. {row[0]} - {row[2]}")
    while True:
        row_number = input("Please enter the number of the entry "
                           "you want to delete: \n")
        if row_number.isdigit() and 1 <= int(row_number) <= len(matching_rows):
            break
        else:
            print("Invalid number. Pls, try again.\n")
    i, row = matching_rows[int(row_number) - 1]
    date = rows[int(row_number)][2]
    goodfood.sheet1.delete_rows(int(row_number), int(row_number))
    print_with_frame(f"You deleted the entry/entries "
                     f"for {food_type} on {date}")


def search_by_date():
    """
    Search for food entries by name, 
    then choose one entry from the displayed ones to delete
    """
    while True:
        date = input("Please enter the date of the food entries "
                     "you want to search for (dd/mm/yyyy): \n")
        try:
            datetime.strptime(date, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date. The date should be in the dd/mm/yyyy format.")
    rows = goodfood.sheet1.get_all_values()
    matching_rows = [row for row in rows if row[2].strip() == date]
    if not matching_rows:
        print(f"No entries found on {date}")
        return
    # Create a table to display the results:
    table = PrettyTable()
    table.field_names = ["Food", "Feeling"]
    for row in matching_rows:
        table.add_row([row[0], row[1]])
    print(table)


def print_with_frame(message):
    """
    Print messages with a frame
    """
    print('+' + '-' * (len(message) + 2) + '+')
    print('| ' + message + ' |')
    print('+' + '-' * (len(message) + 2) + '+')


# Call the menu function to run the programme
menu()
