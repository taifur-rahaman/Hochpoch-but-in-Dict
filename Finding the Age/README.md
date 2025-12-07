# Finding the Age

This Python program allows users to store people's names with their date of birth, display stored information, and calculate ages based on the current year.

### Features


1. Add Information
   * Prompts the user for a name and date of birth.
   * Only accepts the DD/MM/YYYY format using regular expression validation.
2. Display Information
   * Shows all stored names and their corresponding date of birth.
3. Calculate Age
   * Calculates a person’s age by comparing their birth year with the current year.
4. Exit
   * Safely terminates the program.

### How It Works

* Data is stored in a dictionary where:

```python
  key = person's name  
  value = date of birth (DD/MM/YYYY)
```

* The program validates date format using regex: `^\d{2}/\d{2}/\d{4}$ `
* The age calculation subtracts the birth year from the current year.

### Usage

* Run the script.
* Follow the on-screen menu options:

```python
  1 → Add user information  
  2 → Display all saved information  
  3 → Calculate age of a specific person  
  0 → Exit
```

### Notes

* The program only validates the string format of the date, not real calendar validity.
* Names are case-sensitive when calculating age.
  * For example, "Alice" and "alice" are treated as different people.
    * To avoid confusion, enter names consistently (e.g., always capitalize the first letter).


