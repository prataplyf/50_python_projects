import random
import numpy as np
country = ['australia', 'austria', 'argentina', 'bangladesh', 'bahrain', 'brazil', 'canada', 
         'chile', 'cuba', 'denmark', 'djibouti', 'dominican republic', 'egypt', 'estonia', 'ecuador',
         'fiji', 'finland', 'france', 'germany', 'ghana', 'guyana', 'haiti', 'hungary', 'honduras',
         'iceland', 'india', 'ireland', 'jamaica', 'japan', 'jordon', 'kazakhstan', 'kenya', 'korea',
         'laos', 'lebanon', 'liberia', 'maldives', 'mali', 'madagascar', 'namibia', 'nepal', 'norway',
         'oldenburg', 'oman', 'orange free state', 'pakistan', 'peru', 'philippines', 'romania',
         'russia', 'rwanda', 'samoa', 'serbia', 'spain', 'tajikistan', 'tanzania', 'turkmenistan',
         'uganda', 'ukraine', 'uzbekistan', 'vanuatu', 'venezuela', 'vietnam', 'wurttemberg', 'yemen', 
         'zambia']

print('Here is list of countries, in that system randomly choose one country')
print('you need to guess that country, you have 10 limit \n\n')
print(country)

life = 10
remaining_life = 0


def hangman_game():
    choose = random.choice(country)
    print(choose)
    global life, remaining_life
    life = 10
    play = True
    while play:
        user_input = input("Guess the country from the list: ")
        if life == 0:
            print("you loose the game, correct answer is: {}".format(choose))
            print("want to play again  --> \npress ENTER to continue the game\npress q | Q to quit the game")
            replay = input(": ")
            if replay == 'q' or replay == 'Q':
                play = False
                break
            else:
                life = 10
                hangman_game()
        elif user_input in country:
            if user_input == choose:
                life -= 1
                print("Correct Answer, amazing you won the Hangman game")
                print("Do you want to play it again")
                print("Press ENTER to continue the game. \nPress q | Q to quit the game")
                replay = input(": ")
                if replay == 'q' or replay == 'Q':
                    play = False
                    break
                else:
                    life = 10
                    hangman_game()
            else:
                life -= 1
                print("wrong answer, you have {} remaining life.".format(life))
        else:
            life -= 1
            print("Coountry doesn't exist in our list, you have {} remaining life.".format(life))

        



hangman_game()



















