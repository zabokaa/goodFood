# :purple_circle: *Good Food* :purple_circle:

GoodFood Tracker is a Python application that interacts with Google Sheets to track your food intake and feelings associated with it. It provides a simple console-based interface to add, delete, and search for food entries.

The deployed version can be found [here](https://goodfood-bab2ce8696d3.herokuapp.com/).

## Table of Contents

- [Objective](#objective)
- [User Stories](#user-stories)
- [Key Features](#key-features)
- [Code Structure](#code-structure)
- [Testing](#testing)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Project Status](#project-status)
- [Acknowledgements](#acknowledgements)

## Objective

## User Stories

- As a user, I want to add a new food entry so that I can keep track of what I eat and how it makes me feel.

- As a user, I want to see the average feeling of a type of food I ate so that I can understand how different foods affect my mood and well-being.

- As a user, I want to delete a food entry so that I can correct mistakes or remove entries that are no longer relevant.

- As a user, I want to search for food entries by date so that I can review what I ate and how I felt on a specific day.

- As a user, I want to exit the application so that I can end my session when I'm done using the food tracker.

- As a user, I want to see messages printed with a frame so that important information stands out in the console output.

- As a user, I want to interact with a menu so that I can easily choose the operation I want to perform.

- As a user, I want to see validation messages when I enter invalid input so that I can correct my mistakes and learn how to use the application correctly.

- As a user, I want the input for food type to be case-insensitive, so I don't have to worry about the capitalization of my entries.

- As a user, I want to see a table of search results so that I can easily understand and review the data.

- As a user, I want to interact with a Google Sheets document so that my food entries are saved and can be accessed and analyzed later.

## Key Features

### Add a new food entry

- You can add a new food entry with the type of food, your feeling after eating the food (on a scale of 1 to 5).
- The current date will be stored automatically.

### See the average feeling of a typ of food you ate

- You can calculate the average feeling for a specific type of food.

### Delete a food entry for a specific day

- You can delete a food entry by specifying the type of food and the date of the entry.

### Search for food entries by day

- You can search for all food entries on a specific date.
- The results will be displayed in a table.

## Code Structure

The code is structured into the folowing functions:

- menu(): Displays the menu and handles the user's choice.
- add_food_entry(): Adds a new food entry.
- average_feeling(): Calculates the average feeling for a specific type of food.
- delete_food_entry(): Deletes a food entry.
- search_by_date(): Searches for food entries by date.
- print_with_frame(): Prints messages with a frame.


## Testing

## Technologies

## Project Status

Project is: finished

## Deployment

## Acknowledgements

This project was based on full-stack course @ Code Institute.
And an forever thank you 💜 to stackoverflow.
