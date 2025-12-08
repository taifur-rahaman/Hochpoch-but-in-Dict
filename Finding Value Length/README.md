# Finding Value Length

This Python program allows users to search for English words, retrieve their definitions from a local dictionary library, and store them in a personal list for display.

### Features
1. Add Word
   - Prompts the user for a word.
   - Validates if the word exists in the `english-dictionary` database.
   - If found, retrieves and formats the definition before saving it.

2. Show Words
   - Displays all words currently stored in the user's list.
   - Shows the word (Title Case), the character length of the definition, and the definition itself.

3. Exit
   - Prints a goodbye message and safely terminates the program.

### How It Works
- Data is stored in a dictionary where:
 ```markdown
  key = the English word (lowercase)
  value = the definition string
 ```

- The program relies on the external library `english-dictionary` to fetch definitions via `get_dict()`.
- Input validation uses `.casefold()` to ensure case-insensitive lookups (e.g., "Apple" and "apple" are treated the same).
- Definitions are cleaned up using `.strip(": ")` and capitalized before storage.

### Usage
- Ensure the required library is installed:
  pip install english-dictionary
- Run the `main.py` script.
- Follow the on-screen menu options:
```python
  1 → Add a new word to your list
  2 → Show all stored words and definitions
  0 → Exit the application
```

### Notes
- You must install the `english-dictionary` package for this code to run.
- If a word is not found in the database, the program prints "Word Not Found" and does not save it.
- The "Show Words" feature displays the length of the definition string for reference.