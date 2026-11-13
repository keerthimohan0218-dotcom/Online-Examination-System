
from exam import OnlineExam
from admin import Admin
from student import Student

exam = OnlineExam()

admin = Admin(exam)
student = Student(exam)

while True:
    print("\n===== ONLINE EXAMINATION SYSTEM =====")
    print("1. Admin")
    print("2. Student")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        admin.admin_login()

    elif choice == "2":
        student.student_menu()

    elif choice == "3":
        print("Thank you for using Online Examination System!")
        break

    else:
        print("Invalid choice!")
