import random

correct = 'you guessed correctly!'
too_low = 'Too Low!!!'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 1000


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    try:
      return int(input('Guess the secret number? '))
    except ValueError:
      print('You did not enter a number.')
      exit()
      


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def end_game():
    '''get user input to end game'''
    user_input =  input('Do you want to end the game? Press y to end. Press any key to play again ')
    return user_input.lower() == 'y'

def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)
    counter = 0
    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        counter = counter +1
        print(result)

        if result == correct:
            print(f'You guessed {counter} times')
            counter = 0
            if end_game():
              break
    

if __name__ == '__main__':
    main()
