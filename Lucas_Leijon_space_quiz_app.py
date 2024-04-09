questions = [
    {
        "question": "In the quest for interstellar travel, which theoretical propulsion concept proposes the manipulation of spacetime curvature to achieve faster-than-light travel?",
        "options": [
            "A: Alcubierre drive",
            "B: Bussard ramjet",
            "C: Dyson sphere",
            "D: Kardashev scale"
        ],
        "answer": "A"
    },
    {
        "question": "Among the newly discovered exoplanets, which type of exoplanetary system exhibits a configuration where multiple planets orbit around two stars?",
        "options": [
            "A: Hot Jupiters",
            "B: Circumbinary planets",
            "C: Super-Earths",
            "D: Rogue planets"
        ],
        "answer": "B"
    },
    {
        "question": "Concerning planetary exploration, what innovative technology has been utilized to retrieve samples from celestial bodies like asteroids and comets, enabling detailed analysis on Earth?",
        "options": [
            "A: X-ray diffraction (XRD)",
            "B: Chromatography",
            "C: Laser-induced breakdown spectroscopy (LIBS)",
            "D: Atomic force microscopy (AFM)"
        ],
        "answer": "C"
    },
    {
        "question": "Regarding the search for extraterrestrial intelligence (SETI), which phenomenon poses a challenge in detecting potential alien civilizations due to their signals being obscured by natural astrophysical sources?",
        "options": [
            "A: Fast radio bursts (FRBs)",
            "B: Cosmic microwave background radiation",
            "C: Galactic cosmic rays",
            "D: Pulsars"
        ],
        "answer": "A"
    },
    {
        "question": "In the domain of space debris mitigation, what proposed technique aims to remove defunct satellites and debris from orbit by capturing them and either deorbiting or repurposing them?",
        "options": [
            "A: Solar sail propulsion",
            "B: Laser ablation",
            "C: Space harpoon",
            "D: Electrodynamic tether"
        ],
        "answer": "D"
    }
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
