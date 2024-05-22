# Define a list of questions and answers
quiz = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "What is the largest planet in our Solar System?", "answer": "Jupiter"},
    {"question": "Who wrote 'Hamlet'?", "answer": "Shakespeare"}
]

# Function to run the quiz
def run_quiz(quiz):
    score = 0
    for item in quiz:
        print(item["question"])
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == item["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is {item['answer']}.")
        print()

    print(f"Your final score is {score} out of {len(quiz)}.")


run_quiz(quiz)
