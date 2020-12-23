#2nd time taking invalid input
user_choice = input('rock, paper or scissors? ')

if (user_choice != 'rock' and
        user_choice != 'paper' and
            user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')
print('User chose', user_choice)


'''
a && b && c
t && t && t -> True

if (True)  user_choice = input('rock, paper or scissors? ')
if (False) print('User chose', user_choice)

if (condition = True): do this
whatever
'''
