#Guessing game

secret_number = 5
guess = int(input('Enter your guess: '))

while guess != secret_number:
    if guess > secret_number:
        print('Your guess is too high')
    elif guess < secret_number:
        print('Your guess is too low')
    guess = int(input('Enter your guess: '))

print('Congratulations, you won!')   