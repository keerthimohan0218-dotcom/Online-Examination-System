
import json

class Student:

    def __init__(self, exam):
        self.exam = exam

        try:
            with open("students.json", "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = []

    def save_students(self):
        with open("students.json", "w") as file:
            json.dump(self.students, file, indent=4)

    def student_registration(self):
        username = input("Enter Username: ")

        for student in self.students:
            if student["username"] == username:
                print("Username already exists!")
                return

        password = input("Enter Password: ")

        student = {
            "username": username,
            "password": password
        }

        self.students.append(student)
        self.save_students()

        print("Registration Successful!")

    def student_login(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        for student in self.students:
            if student["username"] == username and student["password"] == password:
                print("Login Successful!")
                self.exam.take_exam(username)
                return

        print("Invalid Username or Password!")

    def student_menu(self):
        while True:
            print("\n===== STUDENT MENU =====")
            print("1. Registration")
            print("2. Login")
            print("3. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.student_registration()

            elif choice == "2":
                self.student_login()

            elif choice == "3":
                break

            else:
                print("Invalid choice!")
