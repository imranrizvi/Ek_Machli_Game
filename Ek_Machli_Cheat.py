import random
import string

WORDS = ['Machli', 'Pani me gayi', 'Chhapak']

def generate_random_player():
    name = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    out = False  # Default value for is_out is False
    return {'player_name': name, "is_out": out}

def main():
    num_players = int(input("\nEnter the number of players: "))
    
    enter_player_names= input("\nDo you want to enter player names? (1/0): ")
    
    if enter_player_names == "1":
        players = [input(f"\nEnter the name of player {i+1}: ") for i in range(num_players)]
    else:
        players = [generate_random_player() for _ in range(num_players)]
        print(f"\nGenerated random player names: {print([player['player_name'] for player in players])}")
    
    my_position = int(input('Enter your position (1,2,3...)'))
    my_name = players[my_position-1]['player_name']
    print(f'Your name is {my_name}')

    play_or_cheat = input("\nDo you want to Play(1) or Cheat(0)? (1/0): ")

    play_game(players,play_or_cheat,my_position)

def play_game(players,play_or_cheat,my_position):
    your_name = players[my_position-1]['player_name']
    right_answer = 1
    expected_answer_loop=1
    word_reduction_required=1
    while len(players) > 1:
        for player in players:
            current_player_name = player['player_name']
            if player["is_out"]: 
                continue
            if (current_player_name == your_name and play_or_cheat != "1"):
                no_of_wrong_answers_user_input=0
                no_of_wrong_answers_user_input = input('How many players gave wrong answer?')
                no_of_wrong_answers = int(no_of_wrong_answers_user_input) if no_of_wrong_answers_user_input != '3' and no_of_wrong_answers_user_input.isdigit() else 0
                if (no_of_wrong_answers>0):
                    for i in range(no_of_wrong_answers):
                        player_index_to_terminate =  players.index(player)-1
                        player_to_terminate =  players[player_index_to_terminate]
                        print(f'{player_to_terminate} is out')
                        players.pop(player_index_to_terminate)
                        right_answer = 1
                        expected_answer_loop=1
                        word_reduction_required=1
            
            answer = str(right_answer)
            
            if(play_or_cheat=="1"):
                # Prompt the player for their input
                answer = input(f"\n{current_player_name}, enter the word's number (1 for '{expected_answer_loop} Machli', 2 for 'Pani me gayi', 3 for 'Chhapak'): ").strip().capitalize()
            else:
                if (current_player_name == your_name):
                    prefix = expected_answer_loop if right_answer == 1 else ""
                    print (f"\nPlayer {current_player_name} Your Answer is {prefix} {WORDS[right_answer-1]} ,  answer_loop = {expected_answer_loop}, word_reduction_required = {word_reduction_required} ")

            # Check if the player's input matches the expected word or its index
            if answer != str(right_answer):
                print(f"\nOops! {current_player_name} said the wrong word. right answer is {right_answer},  {current_player_name} is out!")
                player["is_out"]=True
                right_answer = 1
                expected_answer_loop=1
                word_reduction_required=1
            else:
                if(play_or_cheat=="1"):
                    print ('Right Ansser')      
                if (word_reduction_required>0):
                    word_reduction_required-=1
                
                if (word_reduction_required==0):
                    right_answer += 1
                    word_reduction_required = expected_answer_loop

                if (right_answer > len(WORDS)):
                    #print (f"Because {answer_number} > {len(WORDS)}, thus reseting answer_number to 1")
                    right_answer = 1
                    # Increase round multiplier after each complete cycle of 'Ek Machli', 'Pani me gayi', and 'Chhapak'
                    expected_answer_loop += 1
                    word_reduction_required=expected_answer_loop
                    #print (f"Repeate word {expected_answer_loop} times")

    # Print the winner
    print(f"\nCongratulations, {players[0]['player_name']}! You are the winner!")
    # Restart the game with remaining players
    main()

if __name__ == "__main__":
    main()
