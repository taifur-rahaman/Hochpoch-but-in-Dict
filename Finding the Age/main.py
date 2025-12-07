import infoStorage

person_list = {}

while True:
    user_choice = input("1. Add Information\n2. Display Information\n3. Find out Age\n0. Exit\nEnter Your Choice: ")

    match user_choice:
        case "1":
                person_list.update(infoStorage.get_info())
        case "2":
            if person_list == {}:
                print("No Information Found.\n")
                continue
            infoStorage.display_info(person_list)
        case "3":
            if person_list == {}:
                print("No Information Found.\n")
                continue
            person_name = input("Enter Person Name: ")
            if person_name in person_list.keys():
                age = infoStorage.calculate_age(person_list, person_name)
                print(f"{person_name} was born on {person_list[person_name]} and {age} years old.")
        case "0":
            print("Exiting the Program. Goodbye!")
            exit()
        case _:
            print("Invalid Choice. Please Try Again.\n")

