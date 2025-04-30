#---------------------------------------
#  Question Bank
#    Student B: Hamza Aftab
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What planet is known as the Red Planet?", "Mars"),
        ("What gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
        ("How many bones are in the human body?", "206"),
        ("What part of the plant conducts photosynthesis?", "Leaf"),
        ("What force keeps us on the ground?", "Gravity"),
        ("Which planet has the most moons?", "Saturn"),
        ("What is the hardest natural substance on Earth?", "Diamond"),
        ("What organ pumps blood throughout the body?", "Heart"),
        ("Which vitamin is produced when a person is exposed to sunlight?", "Vitamin D")
    ],
    "Math": [
        ("What is 7 x 8?", "56"),
        ("What is the square root of 64?", "8"),
        ("What is the value of Pi to two decimal places?", "3.14"),
        ("What is 15% of 200?", "30"),
        ("Solve: 5 + (6 x 2) - 4", "13"),
        ("What is 12 squared?", "144"),
        ("What is the result of 100 divided by 4?", "25"),
        ("What is the perimeter of a square with side 5?", "20"),
        ("What is the area of a triangle with base 10 and height 5?", "25"),
        ("What is 9 cubed?", "729")
    ],
    "Geography": [
        ("What is the capital of France?", "Paris"),
        ("Which continent is Egypt part of?", "Africa"),
        ("Which country has the largest population?", "China"),
        ("What is the longest river in the world?", "Nile"),
        ("Which ocean is the largest?", "Pacific"),
        ("Which desert is the largest in the world?", "Sahara"),
        ("What is the capital of Japan?", "Tokyo"),
        ("Which country has the city of Istanbul?", "Turkey"),
        ("Which country is known as the Land Down Under?", "Australia"),
        ("Mount Everest is located in which mountain range?", "Himalayas")
    ]
}

hints = {
    "Science": [
        "2 hydrogen, 1 oxygen", "Named for its red appearance", "Used in photosynthesis",
        "More than 200", "Green part", "Pulls everything down", "Planet with rings",
        "Used in jewelry", "Vital organ", "Sunlight helps synthesize it"
    ],
    "Math": [
        "Less than 60", "Perfect square", "3-point-something", "A fifth of 150",
        "Follow order of operations", "12 x 12", "Quarter of 100", "4 x side length",
        "Half x base x height", "9 x 9 x 9"
    ],
    "Geography": [
        "City of love", "Africa or Asia?", "Over a billion people", "Flows through Egypt",
        "Pacific or Atlantic?", "Hot and sandy", "Samurai country", "Crossroads of Europe and Asia",
        "Southern Hemisphere", "Tallest mountain chain"
    ]
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    try:
        return random.choice(questions[category])
    except (KeyError, IndexError):
        return None, None

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    return player_answer.strip().lower() == correct_answer.strip().lower()

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    if category in questions:
        index = 0
        for pair in questions[category]:
            if pair[0] == question:
                questions[category].pop(index)
                hints[category].pop(index)
                break
            index += 1

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    print(f"\nQuestion: {question}")
    return input("Your Answer: ")

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    if category in questions:
        index = 0
        for pair in questions[category]:
            if pair[0] == question:
                return hints[category][index]
            index += 1
    return "No hint available."

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    print(f"Correct Answer: {correct_answer}\n")

#---------------------------------------
