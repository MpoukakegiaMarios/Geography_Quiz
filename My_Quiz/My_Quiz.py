# My_Quiz.py
import json # Kalei to archeio me tis erwthseis
import random
from datetime import datetime

def run_quiz():

    with open("questions.json", "r") as file:
        questions = json.load(file) # Erwthseis


    random.shuffle(questions) # Anakatevei tis erwthseis


    score = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)


        user_answer = input("Your choice (A/B/C/D): ").strip().upper() # Pairnei thn apantish sou

        if user_answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {q['answer']}")

    print(f"\n🎉 You scored {score} out of {len(questions)}.")


    with open("scores.txt", "a") as f: # Archeio me to istoriko
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Ora gia istoriko
        f.write(f"{now} - Score: {score} out of {len(questions)}\n")


def main_menu(): # Menu
    while True:
        print("\nMenu:\n")
        print("1. Start Quiz")
        print("2. View Past Scores")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1": # Epiloges
            run_quiz()
        elif choice == "2":
            try:
                with open("scores.txt", "r") as f:
                    print("\nPast Scores:")
                    print(f.read())
            except FileNotFoundError:
                print("\nNo scores recorded yet.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()

