
import json

class Admin:

    def __init__(self, exam):
        self.exam = exam

    def admin_login(self):
        print("\n===== ADMIN LOGIN =====")

        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")

        if username == "admin" and password == "admin123":
            print("Admin Login Successful!")
            self.admin_menu()
        else:
            print("Invalid Admin Username or Password!")

    def set_exam_count(self):
        total_questions = len(self.exam.questions)

        print("\nAvailable Questions:", total_questions)

        if total_questions == 0:
            print("Please add questions first!")
            return

        try:
            count = int(input("Enter number of questions for exam: "))
        except ValueError:
            print("Please enter a valid number!")
            return

        if count <= 0 or count > total_questions:
            print("Invalid question count!")
            return

        self.exam.config["exam_count"] = count

        with open("config.json", "w") as file:
            json.dump(self.exam.config, file, indent=4)

        print("Exam configured successfully!")

    def admin_menu(self):
        while True:
            print("\n===== ADMIN MENU =====")
            print("1. Add Question")
            print("2. Display Questions")
            print("3. Set Number of Exam Questions")
            print("4. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.exam.add_question()

            elif choice == "2":
                self.exam.display_questions()

            elif choice == "3":
                self.set_exam_count()

            elif choice == "4":
                print("Admin Logged Out!")
                break

            else:
                print("Invalid choice!")
