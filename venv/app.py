""" This program simulates the game Rock/Paper/Scissors which is a hand game usually played between two people,
    in which each player simultaneously forms one of three shapes with an outstretched hand.

    The program asks the human to enter, 'r', 'p', 's' for "rock", "paper", "scissors", or 'q' to exit the game.*
    Computer randomly choose 'rock', 'paper', or 'scissors' and
    compare it with human choise to determine and report the result to the user.
    The game continues until the human chooses to stop by entering 'q' when asked for a move.

    * Human player can enter both lowercase and uppercase letters.
"""


from random import choice


def get_human_move() -> str:
    """ Ask the user for R, P, or S.  Loop until given a valid input """
    while True:
        user_input: str = input("Please choose 'R', 'P', 'S' or 'Q' to quit: ")

        if user_input.lower() == "q": # converting human choise to lowercase to make it valid even if the character entered is uppercase
            return "quit"
        elif user_input.lower() == "r":
            return "rock"
        elif user_input.lower() == "p":
            return "paper"
        elif user_input.lower() == "s":
            return "scissors"
        else:
            print("ERROR! THE INPUT YOU ENTERED IS NOT VALID.") # invalid input error > loop again


def get_computer_move() -> str:
    """ return the computer's random choice using random.choice """
    move: str = choice(['rock', 'paper', 'scissors'])
    return move


def play_game() -> bool:
    """ play Rock/Paper/Scissors
        The human may enter 'Q' or 'q' any time to stop the game.
        Get the human's move, the computer's move, and print a message with the winner.
        Return a bool to specify if the human wants to play again,
        i.e. False when the human wants to quit or True to play again
    """
    human: str = get_human_move()
    if human == 'quit':  # human wants to quit
        return False

    computer: str = get_computer_move()

    result: str = ""

    if computer == human: # comparing computer and human choices to determine the winner
        result = "Tie!"
    elif computer == "rock" and human == "paper":
        result = "You won!"
    elif computer == "paper" and human == "scissors":
        result = "You won!"
    elif computer == "scissors" and human == "rock":
        result = "You won!"
    elif computer == "rock" and human == "scissors":
        result = "You lost!"
    elif computer == "scissors" and human == "paper":
        result = "You lost!"
    elif computer == "paper" and human == "rock":
        result = "You lost!"

    print(f"Your coice: {human}, Computer choice: {computer}. >>> {result}")

    return True  # play again


def main() -> None:
    """ Play multiple games until the human asks to stop """
    again: bool = True
    while again:
        again = play_game()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
