from All_Users_Data import *
from classes.Admin import Admin
from classes.Teacher import Teacher
from classes.Student import Student
from classes.Parent import Parent

def menu():
    print("Welcome to EduPlatform")
    print("1. Enter as Admin")
    print("2. Enter as Teacher")
    print("3. Enter as Student")
    print("4. Enter as Parent")
    print("5. Exit")

    choice = int(input("Choose an option (1-5): "))

    match choice:
        case 1:
            Admin_menu()

        case 2:
            Teacher_menu()

        case 3:
            Student_menu()

        case 4:
            Parent_menu()

        case 5:
            exit()



def Admin_menu():
    print("Logging in as admin...")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in Platform.admins:
        while password != Platform.admins[username]:
            print("Incorrect password! try again")
        print(f"Welcome {"Admin Full_Name"}. Logged in successfully!")

    # else:
    #   print("This username does not exist. Try Registering first!")
    #   exit()

    print("1. Add User.")
    print("2. Remove User.")
    print("3. Generate report.")
    method = int(input("Choose an option (1-3): "))

    match method:
        case 1: Admin.add_user()

        case 2: Admin.remove_user()

        case 3: Admin.generate_report()



def Teacher_menu():
    print("Logging in as teacher...")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in Platform.teachers:
        while password != Platform.teachers[username]:
            print("Incorrect password! try again")
        print(f"Welcome {"Teacher Full_Name"}. Logged in successfully!")

    print("1. Create Assignment.")
    print("2. Grade Assignment.")
    print("3. View Student Progress.")
    method = int(input("Choose an option (1-3): "))

    match method:
        case 1: Teacher.create_assignment()

        case 2: Teacher.grade_assignment()

        case 3: Teacher.view_student_progress()



def Student_menu():
    print("Logging in as student...")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in Platform.students:
        while password != Platform.students[username]:
            print("Incorrect password! try again")
        print(f"Welcome {"Student Full_Name"}. Logged in successfully!")

    print("1. Submit Assignment.")
    print("2. View Grades.")
    print("3. Calculate Average Grade.")
    method = int(input("Choose an option (1-3): "))

    match method:
        case 1: Student.submit_assignment()

        case 2: Student.view_grades()

        case 3: Student.calculate_average_grade()

def Parent_menu():
    print("Logging in as parent...")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in Platform.parents:
        while password != Platform.parents[username]:
            print("Incorrect password! try again")
        print(f"Welcome {"Parent Full_Name"}. Logged in successfully!")

    print("1. View Children Assignments.")
    print("2. View Child Grades.")
    print("3. Receive Child Notification.")
    method = int(input("Choose an option (1-3): "))

    match method:
        case 1: Parent.view_child_assignments()

        case 2: Parent.view_child_grades()

        case 3: Parent.receive_child_notification()

menu()

p1 = Parent()