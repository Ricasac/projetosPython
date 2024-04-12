print('''
 _______________________________________________________________________
|       (_      (_      (_      (_      (_      (_      (_      (_      |
|        _)      _)      _)      _)      _)      _)      _)      _)     |
|  _   _(  _   _(  _   _(  _   _(  _   _(  _   _(  _   _(  _   _(  _   _|
|_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |
|      _)      _)      _)      _)      _)      _)      _)      _)       |
|     (_      (_      (_      (_      (_      (_      (_      (_        |
|_   _  )_   _  )_   _  )_   _  )_   _  )_   _  )_   _  )_   _  )_   _  |
| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_|
|       (_      (_      (_      (_      (_      (_      (_      (_      |
|        _)      _)      _)      _)      _)      _)      _)      _)     |
|  _   _(  _   _(  _   _(  _   _(  _   _(  _   _(  _   _(  _   _(  _   _|
|_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |
|      _)      _)      _)      _)      _)      _)      _)      _)       |
|     (_      (_      (_      (_      (_      (_      (_      (_        |
|_   _  )_   _  )_   _  )_   _  )_   _  )_   _  )_   _  )_   _  )_   _  |
| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| |_|
|       (_      (_      (_      (_      (_      (_      (_      (_      |
|        _)      _)      _)      _)      _)      _)      _)      _)     |
|_______(_______(_______(_______(_______(_______(_______(_______(_______|
''')
print('Welcome to Treasure Island. Your mission is to find the treasure.')
choice1 = input('Do you wish to go left or right?')
choice1 = str(choice1.lower())

if choice1 != 'left':
    print('You just got attacked by mountain bandits. Game Over :(')

else:
    choice2 = input('You just arrived at a lake. Do you want to swim or wait for a boat?(please input "swim" or "wait"')
    choice2 = str(choice2.lower())

    if choice2 != 'wait':
        print('You just got attacked by a 7 Alligators. Game over :(')

    else:
        choice3 = input('In front of you, you see 3 doors. One Yellow, one Red and one Blue. Which one do you pick?')
        choice3 = str(choice3.lower())

        if choice3 == 'blue':
            print('As you open the door several beasts jump at you. Game Over :(')

        elif choice3 == 'red':
            print('As you open the door, a sea of flames comes out and surrounds you, burning your body. Game Over :(')

        elif choice3 == 'yellow':
            print('As you open the door you see a treasure box full of gold. It´s your for the taking :) Congrats.')

        else:
            print('You just got jumped by a horde of skeletons, taking your life and turning you into one of them. Game Over :(')