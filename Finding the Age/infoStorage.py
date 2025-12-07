import re
from datetime import date

def find_year(dob):
    return int(dob.split("/")[2])

def get_info():
    while True:    
        name = input("Enter your name: ")
        dob = input("Enter your Date of Birth (DD/MM/YYYY): ")
        pattern = r"^\d{2}/\d{2}/\d{4}$"

        while not re.match(pattern, dob):
            print("Invalid date format. Please enter in the format DD/MM/YYYY.")
            dob = input("Enter your Date of Birth (DD/MM/YYYY): ")
            
        person_info = {name : dob}
        print("Information Added")
        break
    return person_info

def display_info(person_info):
    for key, value in person_info.items():
        print(f"{key.title()} : {value}")

def calculate_age(person_list, person_name):
    dob = person_list[person_name]
    age = date.today().year - find_year(dob)
    return age
    