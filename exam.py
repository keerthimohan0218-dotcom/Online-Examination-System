
import json
import random

class OnlineExam:

    def __init__(self):
        try:
            with open("questions.json", "r") as file:
                self.questions = json.load(file)
        except FileNotFoundError:
            self.questions = []

        try:
            with open("config.json", "r") as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = {"exam_count": 0}

    def save_questions(self):
        with open("questions.json", "w") as file:
            json.dump(self.questions, file, indent=4)

    def add_question(self):
        question = input("Enter Question: ")

        options = {}
        options["A"] = input("Option A: ")
        options["B"] = input("Option B: ")
        options["C"] = input("Option C: ")
        options["D"] = input("Option D: ")

        answer = input("Enter Correct Answer (A/B/C/D): ").upper()

        if answer not in options:
            print("Invalid Answer!")
            return

        data = {
            "question": question,
            "options": options,
            "answer": answer
        }

        self.questions.append(data)
        self.save_questions()

        print("Question added successfully!")

    def display_questions(self):
        if not self.questions:
            print("No questions available.")
            return

        print("\n===== AVAILABLE QUESTIONS =====")

        for i, q in enumerate(self.questions, 1):
            print(f"\nQ{i}. {q['question']}")

            for key, value in q["options"].items():
                print(key, ".", value)

    def take_exam(self, username):
        exam_count = self.config["exam_count"]

        if exam_count <= 0:
            print("Admin has not configured the exam yet!")
            return

        if exam_count > len(self.questions):
            print("Not enough questions available!")
            return

        selected_questions = random.sample(self.questions, exam_count)

        score = 0

        print("\n===== ONLINE EXAM =====")
        print("Total Questions:", exam_count)

        for i, q in enumerate(selected_questions, 1):
            print(f"\nQ{i}. {q['question']}")

            for key, value in q["options"].items():
                print(key, ".", value)

            answer = input("Enter your answer (A/B/C/D): ").upper()

            if answer == q["answer"]:
                print("Correct Answer!")
                score += 1
            else:
                print("Wrong Answer!")

        total = exam_count
        percentage = (score / total) * 100

        print("\n===== EXAM RESULT =====")
        print("Student Name:", username)
        print("Total Questions:", total)
        print("Correct Answers:", score)
        print("Wrong Answers:", total - score)
        print("Total Marks:", score)
        print("Percentage:", percentage, "%")

        if percentage >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")

        self.save_result(username, score, total, percentage)

    def save_result(self, username, score, total, percentage):
        try:
            with open("results.json", "r") as file:
                results = json.load(file)
        except FileNotFoundError:
            results = []

        result = {
            "username": username,
            "score": score,
            "total": total,
            "percentage": percentage
        }

        results.append(result)

        with open("results.json", "w") as file:
            json.dump(results, file, indent=4)

        print("Result saved successfully!")
