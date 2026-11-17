import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1)

# Convert toss number to heads/tails
if toss == 1:
    result = 'heads'
else:
    result = 'tails'

# Debugging checkpoint
breakpoint()

if result == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')

    guess = input('Enter heads or tails: ')

    if result == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')