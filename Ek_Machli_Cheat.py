import random
import string

WORDS = ['Ek Machli', 'Pani me gayi', 'Chhapak']

def main():
    num_players = int(input("\nEnter the number of players: "))
    
    enter_player_names= input("\nDo you want to enter player names? (1/0): ")
    
    if enter_player_names == "1":
        players = [input(f"\nEnter the name of player {i+1}: ") for i in range(num_players)]
    else:
        players = [generate_random_name() for _ in range(num_players)]
        print(f"\nGenerated random player names: {players}")
    
    show_answers = input("\nDo you want to show answers? (1/0): ")

    play_game(players,show_answers)

def play_game(players,show_answers):
    answer_number = 1
    expected_answer_loop=1
    word_reduction_required=1
    while len(players) > 1:
        for player in players:
            if(show_answers=="1"):
                print (f"\nNext Answer = {answer_number} {WORDS[answer_number-1]}")
            
            # Prompt the player for their input
            guess = input(f"\n{player}, enter the word's number (1 for 'Ek Machli', 2 for 'Pani me gayi', 3 for 'Chhapak'): ").strip().capitalize()

            # Check if the player's input matches the expected word or its index
            if guess != str(answer_number):
                print(f"\nOops! {player} said the wrong word. {player} is out!")
                players.remove(player)
                answer_number = 1
                expected_answer_loop=1
                word_reduction_required=1
            else:
                if (word_reduction_required>0):
                    word_reduction_required-=1
                
                if (word_reduction_required==0):
                    answer_number += 1
                    word_reduction_required = expected_answer_loop

                if (answer_number > len(WORDS)):
                    #print (f"Because {answer_number} > {len(WORDS)}, thus reseting answer_number to 1")
                    answer_number = 1
                    # Increase round multiplier after each complete cycle of 'Ek Machli', 'Pani me gayi', and 'Chhapak'
                    expected_answer_loop += 1
                    word_reduction_required=expected_answer_loop
                    #print (f"Repeate word {expected_answer_loop} times")

    # Print the winner
    print(f"\nCongratulations, {players[0]}! You are the winner!")
    # Restart the game with remaining players
    main()

def generate_random_name():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

if __name__ == "__main__":
    main()
