#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
# Ebaad ur Rehman (281163937)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
 
    
    print("WELCOME TO THE TRIVIA GAME!!!") 
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
   
    print("Choose a category:")
    for i in range(len(categories)):
        print(f"{i+1}. {categories[i]}")
    
    choice = int(input("Enter your choice (number): "))  
    return categories[choice-1] 

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
 
    
    print(f"ROUND: {round_number}")
    print(f"Your current score: {score}")
    

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    
    message = "GAME OVER!"
    print(message)
    print("=" * 20)
    print(f"Your Final Score: {final_score}")
    
    if final_score > 10:
        print("WOW! You're a genius!")
    elif final_score > 5:
        print("Good job!")
    else:
        print("Better luck next time...")
    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
   
    round = 1
    score = 0
    
    while round <= 5:
        print(f"Round {round}")
        category = choose_category(categories)
        
        print(f"Playing with category: {category}")
        
        score = score + round
        round = round + 1  
    
    print(f"Game finished! Final score: {score}")
    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """

    if player_answer == correct_answer:
        return True
    else:
        return False  
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
   
    points = 0
    
    if correct == True: 
        points = 10
    
    new_score = score + points
    return new_score
    #------------------------

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
   
    round_number = round_number + 1  
    return round_number
    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
   
    max_wrong = 3
    is_game_over = False
    
    if incorrect_answers >= max_wrong:
        is_game_over = True
    
    return is_game_over  
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
   
    print("Do you want to play again?")
    choice = input("Enter 'yes' to restart or any other key to exit: ")
    
    if choice.lower() == "yes":
        import main
        print("Restarting game...")
        main.main()
    else:
        print("Thanks for playing! Goodbye!")
       

#---------------------------------------