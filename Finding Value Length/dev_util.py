from english_dictionary.scripts.read_pickle import get_dict

english_dict = get_dict()

def add_word():
    word = input("Enter a Word: ").casefold()
    if word not in english_dict:
        print("Word Not Found")
        return
    definition = english_dict[word].strip(": ").capitalize()
    return {word: definition}

def show_word(user_list):
    for word, meaning in user_list.items():
        print(f"{word.title()} - {len(meaning)} - {meaning}")