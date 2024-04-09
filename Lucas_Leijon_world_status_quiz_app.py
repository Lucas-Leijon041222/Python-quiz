questions = [
    {
        "question": "Which country is currently the world's largest importer of oil?",
        "options": [
            "A: United States",
            "B: China",
            "C: India",
            "D: Japan"
        ],
        "answer": "A"
    },
    {
        "question": "Which global event caused a significant disruption in the supply chain and led to shortages of various goods worldwide?",
        "options": [
            "A: COVID-19 pandemic",
            "B: Brexit",
            "C: Arab Spring",
            "D: Russian invasion of Ukraine"
        ],
        "answer": "A"
    },
    {
        "question": "Which country is currently experiencing ongoing protests and demonstrations due to economic instability and government corruption?",
        "options": [
            "A: Venezuela",
            "B: Brazil",
            "C: Turkey",
            "D: Lebanon"
        ],
        "answer": "D"
    },
    {
        "question": "What is the name of the trade agreement signed between the United States, Mexico, and Canada, aimed at modernizing and rebalancing trade relationships?",
        "options": [
            "A: NAFTA 2.0",
            "B: TPP",
            "C: CPTPP",
            "D: USMCA"
        ],
        "answer": "D"
    },
    {
        "question": "Which country recently launched a digital currency, becoming one of the first major economies to do so?",
        "options": [
            "A: China",
            "B: United States",
            "C: Germany",
            "D: Japan"
        ],
        "answer": "A"
    },
    {
        "question": "Which conflict, ongoing since 2014, has resulted in a significant humanitarian crisis, with millions displaced and thousands killed?",
        "options": [
            "A: Syrian Civil War",
            "B: Yemeni Civil War",
            "C: Rohingya genocide",
            "D: Ukrainian crisis"
        ],
        "answer": "B"
    },
    {
        "question": "Which international organization is currently leading efforts to address climate change through initiatives such as the Paris Agreement?",
        "options": [
            "A: United Nations",
            "B: World Bank",
            "C: International Monetary Fund",
            "D: World Trade Organization"
        ],
        "answer": "A"
    },
    {
        "question": "What term describes the economic policy implemented by some countries to increase domestic production and reduce reliance on imports?",
        "options": [
            "A: Protectionism",
            "B: Globalization",
            "C: Free trade",
            "D: Neoliberalism"
        ],
        "answer": "A"
    },
    {
        "question": "Which country recently faced a military coup resulting in the ousting of its democratically elected government?",
        "options": [
            "A: Myanmar",
            "B: Thailand",
            "C: Egypt",
            "D: Sudan"
        ],
        "answer": "A"
    },
    {
        "question": "Which economic indicator measures the total value of goods and services produced within a country's borders in a specific time period?",
        "options": [
            "A: GDP (Gross Domestic Product)",
            "B: CPI (Consumer Price Index)",
            "C: PPP (Purchasing Power Parity)",
            "D: Gini coefficient"
        ],
        "answer": "A"
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
