import random
n = input("Hello! What is your name? ")
num = random.randint(1, 20)
amt = 0
print(f'Well, {n}, I am thinking of a number between 1 and 20.')
while True:
    g = int(input("Take a guess\n"))
    amt += 1
    if g == num:
        print(f"Good job, {n}! You guessed my number in {amt} guesses!")
        break
    elif g < num:
        print('Your guess is too low')
    else:
        print('Your guess is too high')