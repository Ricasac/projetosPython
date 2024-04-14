import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Hello and welcome to the game of Rock, Paper, Scissors!')
userChoice = int(input('Please chose one of them being Rock, Paper and Scissors -> 0, 1 and 2 respectively'))
cpuChoice = random.randint(1,3)

#cases
if userChoice == 0 and cpuChoice == 1:
    print(rock)
    print('Computer choice: ')
    print(rock)
    print('You Draw!')

elif userChoice == 0 and cpuChoice == 2:
    print(rock)
    print('Computer choice: ')
    print(paper)
    print('You Lose!')

elif userChoice == 0 and cpuChoice == 3:
    print(rock)
    print('Computer choice: ')
    print(scissors)
    print('You Win!')

elif userChoice == 1 and cpuChoice == 1:
    print(paper)
    print('Computer choice: ')
    print(rock)
    print('You Win!')

elif userChoice == 2 and cpuChoice == 2:
    print(paper)
    print('Computer choice: ')
    print(paper)
    print('You Draw!')

elif userChoice == 2 and cpuChoice == 3:
    print(paper)
    print('Computer choice: ')
    print(scissors)
    print('You Lose!')

elif userChoice == 3 and cpuChoice == 1:
    print(scissors)
    print('Computer choice: ')
    print(rock)
    print('You Lose!')

elif userChoice == 3 and cpuChoice == 2:
    print(scissors)
    print('Computer choice: ')
    print(paper)
    print('You Win!')

elif userChoice == 3 and cpuChoice == 3:
    print(scissors)
    print('Computer choice: ')
    print(scissors)
    print('You Draw!')

else:
    print('What you inputted is not valid. Please try again.')