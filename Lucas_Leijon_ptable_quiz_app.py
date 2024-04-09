questions = [
    {
        "question": "What is the chemical symbol for hydrogen?",
        "options": [
            "A: H",
            "B: He",
            "C: O",
            "D: Au"
        ],
        "answer": "A"
    },
    {
        "question": "Which element has the atomic number 6?",
        "options": [
            "A: Carbon",
            "B: Nitrogen",
            "C: Oxygen",
            "D: Helium"
        ],
        "answer": "A"
    },
    {
        "question": "What is the symbol for gold?",
        "options": [
            "A: G",
            "B: Au",
            "C: Ag",
            "D: Fe"
        ],
        "answer": "B"
    },
    {
        "question": "Which element is a noble gas?",
        "options": [
            "A: Oxygen",
            "B: Nitrogen",
            "C: Helium",
            "D: Sodium"
        ],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for iron?",
        "options": [
            "A: F",
            "B: Ir",
            "C: Fe",
            "D: In"
        ],
        "answer": "C"
    },
    {
        "question": "Which element is commonly used in batteries?",
        "options": [
            "A: Helium",
            "B: Lithium",
            "C: Neon",
            "D: Boron"
        ],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for sodium?",
        "options": [
            "A: So",
            "B: Sn",
            "C: Na",
            "D: Ni"
        ],
        "answer": "C"
    },
    {
        "question": "Which element has the atomic number 26?",
        "options": [
            "A: Iron",
            "B: Zinc",
            "C: Silver",
            "D: Copper"
        ],
        "answer": "A"
    },
    {
        "question": "What is the symbol for helium?",
        "options": [
            "A: H",
            "B: He",
            "C: Hy",
            "D: Hm"
        ],
        "answer": "B"
    },
    {
        "question": "Which element is commonly used in pencils?",
        "options": [
            "A: Carbon",
            "B: Nitrogen",
            "C: Oxygen",
            "D: Neon"
        ],
        "answer": "A"
    },
    {
        "question": "What is the electron affinity of hydrogen?",
        "options": [
            "A: -73 kJ/mol",
            "B: -52 kJ/mol",
            "C: -200 kJ/mol",
            "D: +73 kJ/mol"
        ],
        "answer": "A"
    },
    {
        "question": "What is the electron affinity of helium?",
        "options": [
            "A: -48 kJ/mol",
            "B: -41 kJ/mol",
            "C: -32 kJ/mol",
            "D: +21 kJ/mol"
        ],
        "answer": "B"
    },
    {
        "question": "What is the electron affinity of lithium?",
        "options": [
            "A: -60 kJ/mol",
            "B: -32 kJ/mol",
            "C: -48 kJ/mol",
            "D: +60 kJ/mol"
        ],
        "answer": "A"
    },
    {
        "question": "What is the electron affinity of beryllium?",
        "options": [
            "A: -48 kJ/mol",
            "B: +4 kJ/mol",
            "C: -20 kJ/mol",
            "D: +61 kJ/mol"
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
