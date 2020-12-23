#Rock,Paper & Scissors (Game)

#We are importing randome module for randomly choice and setting winner variable as a empty string. 
import random
winner = ''

#random_choice is a variable,And random.randint is a function which will take random number within 0,1&2.
#then the 0,1,2 will be assigned in rock,paper and scissors.
random_choice = random.randint(0,2)
if random_choice == 0:
    computer_choice = 'rock'
    
elif random_choice == 1:
    computer_choice = 'paper'
    
else:
    computer_choice = 'scissors'
    
#prompting to give input and matching with the computer's choice and user input. Condition set up for providing the result.
user_choice = input('rock, paper or scissors? ')
if computer_choice == user_choice:
    winner = 'Tie'
    
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
    
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
    
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
    
else:
    winner = 'User'
    
#Reslut Showing.
if winner == 'Tie':
    print('We both chose', computer_choice + ', play again.')
    
else:
    print(winner, 'won. The computer chose', computer_choice + '.')
