import random, sys

print("")
print('ROCK', 'PAPER', 'SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

totalGames = wins + losses + ties

# This is the main game loop
while True:
    print(f'ScoreCard: {wins} Wins, {losses} Losses, {ties} Ties')
    print("")
    print('Instructions:Please enter either "Rock", "Paper", "Scissors" or "Quit"')

    # The player input loop
    while True:
        playerMove = input()
        if playerMove == 'Quit':
            sys.exit()
        if playerMove == 'Rock' or playerMove == 'Paper' or playerMove == 'Scissors':
            # Exit the player loop
            break

    # Display what the player chose
    if playerMove == 'Rock':
        print('Rock versus...')
    elif playerMove == 'Paper':
        print('Paper versus...')
    elif playerMove == 'Scissors':
        print('Scissors versus...')

    # Display what the computer chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'Rock'
        print('ROCK')
    if randomNumber == 2:
        computerMove = 'Paper'
        print('PAPER')
    if randomNumber == 3:
        computerMove = 'Scissors'
        print('SCISSORS')

    # Display and record the win/loss/tie
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'Rock' and computerMove == 'Scissors':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'Paper' and computerMove == 'Rock':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'Scissors' and computerMove == 'Paper':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'Rock' and computerMove == 'Paper':
        losses = losses + 1
        print('HAH! You lose.')
    elif playerMove == 'Paper' and computerMove == 'Scissors':
        losses = losses + 1
        print('HAH! You lose.')
    elif playerMove == 'Scissors' and computerMove == 'Rock':
        losses = losses + 1
        print('HAH! You lose.')