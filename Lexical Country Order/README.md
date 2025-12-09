# Lexical Country Order

This Python program organizes and displays all countries in the world alphabetically, grouping them by their starting letter and showing the count of countries for each letter.

## Features
1.  **Alphabetical Grouping**
    -   Automatically groups all countries by their first letter (A-Z).
    -   Uses the comprehensive `pycountry` library for accurate country data.
2.  **Country Count Statistics**
    -   Displays the total number of countries starting with each letter.
    -   Provides a complete overview of country distribution across the alphabet.
3.  **Formatted Display**
    -   Shows countries in a comma-separated list for easy reading.
    -   Presents data in a clean, organized format with letter headings.

## How It Works
-   The program uses the `pycountry` library to access official country names.
-   Data is stored in a dictionary where:
	```python
	key = capital letter (A-Z)value = list of country names starting with that letter
	```
-   The `letter_count()` function generates all uppercase letters using ASCII values (65-90).
-   Countries are dynamically filtered and grouped based on their `.startswith()` method.
-   The output displays each letter, its associated countries, and a count.
## Usage

1.  **Install the required library:**
    ```python
    pip install pycountry
    ```
2.  **Run the script:**
    ```python
    python main.py
    ```
3.  The program will automatically:
    -   Fetch all countries from the `pycountry` database
    -   Group them alphabetically
    -   Display the results with statistics

## Sample Output
```
A : Afghanistan , Albania , Algeria , Andorra , Angola - 
Total Country Starts with A : 5
B : Bahamas , Bahrain , Bangladesh , Barbados , Belarus - 
Total Country Starts with B : 5
C : Cambodia , Cameroon , Canada , Chile , China , Colombia - 
Total Country Starts with C : 6
...
```

## Notes
-   **Required Package:** You must install `pycountry` for this program to work.
-   The program uses official country names from the ISO 3166 standard.
-   Some letters may have no countries (e.g., X), which will show an empty list with count 0.
-   The country data is sourced from the `pycountry` library and may be updated with new releases.
-   Country names are displayed in their official English form as stored in the database.

## Dependencies
```txt
pycountry>=22.3.0
```

## Technical Details

-   **ASCII Range:** Uses `chr(x) for x in range(65, 91)` to generate A-Z
-   **List Management:** Uses `.copy()` to avoid reference issues when clearing the temporary list
-   **String Formatting:** Uses f-strings with `.join()` for clean output formatting