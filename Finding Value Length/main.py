import dev_util as util

user_list = {}

while True:
    choice = input("1. Add Word\n2. Show Words\n0. Exit\nEnter your Choice: ")
    match choice:
        case "1":
            user_list.update(util.add_word())
        case "2":
            util.show_word(user_list)
        case "0":
            print("Thank You For Using the Application\nGoodBye!!!")
            exit()
        case _:
            print("Invalid Input. Please Try Again.")




