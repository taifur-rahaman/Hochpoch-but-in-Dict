
# Student Information System

This Python program allows users to manage student records by adding new students and displaying their information through a simple command-line interface.

## Features

1.  **Add Student**
    -   Prompts the user to enter student details (Name, ID, Department).
    -   Stores the student information in memory for the current session.
    -   Each student is uniquely identified by their name.
2.  **Display Student**
    -   Allows users to search for a student by name.
    -   Displays the student's complete information (Name, ID, Department).
    -   Shows an error message if the student doesn't exist in the system.
3.  **Exit**
    -   Prints a goodbye message and safely terminates the program.

## How It Works

-   Data is stored in a dictionary where:
    ```python
    key = student name (string)
    value = dictionary containing {"Name": {name}, "ID": {id}, "Department": {dept}}
    ```
-   The program uses a modular structure with two files:
    -   `infoStorage.py` - Contains functions for adding and displaying students
    -   `main.py` - Main program loop with menu interface
-   Student information persists only during the current program execution (data is not saved to disk).

## Usage

1.  Run the `main.py` script:
    
    ```bash
    python main.py
    ```
2.  Follow the on-screen menu options:
    ```
    1 → Add a new student to the system
    2 → Display information for a specific student
    0 → Exit the application
    ```
    
3.  When adding a student, provide:
    -   Full name
    -   Student ID
    -   Department name
4.  When displaying a student, enter the exact name used during registration.
    

## Notes

-   No external libraries are required - this program uses only Python standard library features.
-   Student names are case-sensitive (e.g., "John Doe" and "john doe" are treated as different students).
-   Data is not persisted between program runs - all information is lost when the program exits.
-   Each student name must be unique; adding a student with an existing name will overwrite the previous record.