import infoStorage

students = {}


while True:
    choice = input("1. Add Student\n2. Display Student\n0. Exit\nEnter your Choice: ")
    
    match choice:
        case "1":
            students.update(infoStorage.add_student())
        case "2":
            student_name = input("Enter Student Name to his/her Information: ")
            infoStorage.display_student(students, student_name)
        case "0":
            print("Thank You for Using the Application\nGoodBye!!!")
            break
        case _:
            print("Invalid Input. Please Try Again.")