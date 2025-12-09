
def add_student():
    student = {}
    
    student_name = input("Enter Your Name: ")
    student_id = input("Enter Your ID: ")
    student_dept = input("Enter Your Department Name: ")
    
    student.update({student_name: {"Name" : {student_name}, "ID" : {student_id}, "Department" : {student_dept}}})
    
    return student

def display_student(students, student_name):
    if student_name in students:
        print(f"Name: {students[student_name].get("Name")}\nID: {students[student_name].get("ID")}\nDepartment: {students[student_name].get("Department")}")
    else:
        print("Student don't Exist")