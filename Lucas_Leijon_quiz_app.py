questions = [
    {
        "question": "How do you convert a decimal to a hex ?",
        "options": [
            "A: Using the division method",
            "B: Subtracting successive powers of 16",
            "C: Dividing by 16 repeatedly and noting remainders",
            "D: Multiplying by 16 repeatedly and noting the digits",
        ],
        "answer": "C"
    },
    {
        "question": "Which of the following statements is true about Python's list comprehensions?",
        "options": [
            "A: They can contain an arbitrary number of for and if clauses.",
            "B: They can only be used to create lists of numbers.",
            "C: They can only be used with built-in functions.",
            "D: They can only be used to modify existing lists.",
        ],
        "answer": "A"
    },
    {
        "question": "What does the `lambda` keyword do in Python?",
        "options": [
            "A: Declares a constant value.",
            "B: Creates an anonymous function.",
            "C: Initializes a class instance.",
            "D: Defines a global variable.",
        ],
        "answer": "B"
    },
    {
        "question": "In Python, what is the purpose of the `elif` keyword?",
        "options": [
            "A: It indicates the beginning of a new function definition.",
            "B: It signifies the end of a loop.",
            "C: It is used to handle multiple conditions after an initial `if` statement.",
            "D: It is a syntax error and should not be used.",
        ],
        "answer": "C"
    },
    {
        "question": "What is the output of `print(9//2)` in Python?",
        "options": [
            "A: 4.5",
            "B: 9",
            "C: 5",
            "D: 4",
        ],
        "answer": "D"
    },
    {
        "question": "What does the `pass` statement do in Python?",
        "options": [
            "A: It is a placeholder that does nothing.",
            "B: It generates a runtime error.",
            "C: It terminates the program immediately.",
            "D: It is used to skip the current iteration of a loop.",
        ],
        "answer": "A"
    },
    {
        "question": "What is the purpose of the `zip()` function in Python?",
        "options": [
            "A: To compress files.",
            "B: To create a zip archive.",
            "C: To combine elements from multiple iterables into tuples.",
            "D: To unzip files.",
        ],
        "answer": "C"
    },
    {
        "question": "Which of the following is NOT a valid data type in Python?",
        "options": [
            "A: List",
            "B: Dictionary",
            "C: Tuple",
            "D: String",
        ],
        "answer": "D"
    },
    {
        "question": "What does the `__init__` method do in Python classes?",
        "options": [
            "A: Initializes the object's attributes.",
            "B: Terminates the program.",
            "C: Initializes the Python interpreter.",
            "D: Deletes the object.",
        ],
        "answer": "A"
    },
    {
        "question": "What is the output of `print('Hello' + 'world')` in Python?",
        "options": [
            "A: Hello world",
            "B: Helloworld",
            "C: Hello + world",
            "D: Error",
        ],
        "answer": "B"
    },
]

def run_quiz(questions):
    score = 0  

    for question in questions:
        print("\n" + question["question"])  
        for option in question["options"]:
            print(option)

        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  
        else:
            print("Wrong answer.")

    print(f"\nYou got {score} out of {len(questions)} questions correct!")

run_quiz(questions)
