nums = list(range(1, 100))

while len(nums) > 0:
  print(nums.pop())

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('You correctly guessed it!')
      return False
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()

# Exercise Guide

def loop_using_while():
    dog_house = ['Linda', 'Kira', 'Dama', 'Yago'] 
    counter = 0

    while counter < len(dog_house):
        print(dog_house[counter])
        counter += 1

    return [dog_house, counter]

loop_using_while()