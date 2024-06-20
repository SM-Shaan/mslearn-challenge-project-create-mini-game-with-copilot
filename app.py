# write 'hello world' to the console
print('Hello World')
#Create a multiplayer game where one player is the computer and the other player is a human.
# The game is a rock-paper-scissors.
# The computer randomly selects rock, paper, or scissors.
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.


import random

def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    while True:
        player_input = input('Enter rock, paper, or scissors: ').lower()
        if player_input not in options:
            print('Invalid option. Please enter rock, paper, or scissors.')
            continue
        computer_input = random.choice(options)
        print(f'Computer chose {computer_input}')
        if player_input == computer_input:
            print('Tie!')
        elif (player_input == 'rock' and computer_input == 'scissors') or (player_input == 'paper' and computer_input == 'rock') or (player_input == 'scissors' and computer_input == 'paper'):
            print('You won!')
            player_score += 1
        else:
            print('You lost!')
            computer_score += 1
        print(f'Player: {player_score} - Computer: {computer_score}')
        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again == 'no':
            break
    print(f'Final score: Player: {player_score} - Computer: {computer_score}')

rock_paper_scissors()

