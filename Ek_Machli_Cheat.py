import random
import string

WORDS = ['Machli', 'Pani me gayi', 'Chhapak']

def generate_random_player():
    name = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    out = False  # Default value for is_out is False
    return {'player_name': name, "is_out": out}

def announce_winner(players):
    # Print the winner
    print(f"\nCongratulations, {players[0]['player_name']}! You are the winner!")
    return True

def main(min_iteration):
    num_players = int(input("\nEnter the number of players: "))
    
    enter_player_names= input("\nDo you want to enter player names? (1/0): ")
    
    if enter_player_names == "1":
        players = [{'player_name': input(f"\nEnter the name of player {i+1}: "), 'is_out': False} for i in range(num_players)]
    else:
        players = [generate_random_player() for _ in range(num_players)]
        print(f"\nGenerated random player names: {print([player['player_name'] for player in players])}")
    
    play_or_cheat = input("\nDo you want to Play(1) or Cheat(0)? (1/0): ")

    play_game(players,play_or_cheat,min_iteration)

def play_game(players,play_or_cheat,min_iteration):
    right_answer = 1
    expected_answer_loop=1
    word_reduction_required=1
    active_player_count = len([player for player in players if not player['is_out']]) 
    fair_play = play_or_cheat=="1"
    if (not fair_play): #cheat
        my_position = int(input('Enter your position (1,2,3...)'))
        your_name = players[my_position-1]['player_name']
        print(f'Your name is {your_name}')

    while active_player_count> 1 and min_iteration>0:
        print (f'active players = {active_player_count}')
        min_iteration-=1
       
        for player in players:
            # current_player_index  = next((i for i, p in enumerate(players) if p == player), None)
            # print (current_player_index)
            current_player_name = player['player_name']
            if player["is_out"]: 
                continue

            if (not fair_play): #cheat
                if (current_player_name == your_name):
                    players_out=0
                    players_out = input('How many players gave wrong answer?')
                    players_out_int = int(players_out) if players_out.isdigit() else 0
                    if (players_out_int>0):
                        for i in range(players_out_int):

                            player_index_to_terminate =  players.index(player)-1
                            player_to_terminate =  players[player_index_to_terminate]
                            player_to_terminate['is_out']=True
                            active_player_count -=1
                            print(f'{player_to_terminate} is out')
                            # players.pop(player_index_to_terminate)
                            right_answer = 1 #reset the right answer to Ek Machili
                            expected_answer_loop=1 #reset the word repeatation to 1
                            word_reduction_required=1
                    prefix = expected_answer_loop if right_answer == 1 else ""
                    print (f"\nPlayer {current_player_name} Your Answer is {prefix} {WORDS[right_answer-1]} ,  answer_loop = {expected_answer_loop}, word_reduction_required = {word_reduction_required} ")
                answer = str(right_answer)
            else: #fair play
                # Prompt the player for their input
                answer = input(f"\n{current_player_name}, select your choice (1 for '{expected_answer_loop} Machli', 2 for 'Pani me gayi', 3 for 'Chhapak'): ").strip().capitalize()

            # Check if the player's input matches the expected word or its index
            if answer != str(right_answer):
                print(f"\nOops! {current_player_name} said the wrong word. right answer is {right_answer},  {current_player_name} is out!")
                player["is_out"]=True
                active_player_count -=1
                right_answer = 1
                expected_answer_loop=1
                word_reduction_required=1
                # current_player_index = [player['player_name'] for player in players].index(current_player_name) 
                # print(f'Start new roun3d with {active_player_count}, player {players[current_player_index+1]['player_name']} to make first call')
            else:
                if (fair_play): #cheat
                    print ('Right Answer')      

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
                
                if (active_player_count<=1):
                    break

    announce_winner(players)
    main(100)

if __name__ == "__main__":
    main(100)
