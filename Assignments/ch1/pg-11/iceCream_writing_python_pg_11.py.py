#For randomly choice; we need import keyword and random module.
import random
customers = ['Jimmy', 'kim', 'John', 'Stacie']

#Choose one customer randomly and put the value as winner.
winner = random.choice(customers)

#Set a variable named flavor to the text vanilla.
flavor = 'vanilla'

#Printing Congratulations,
#Name of the winner which was chosen randomly as winner
#And you have won an ice cream sundae!
print('Congratulations ' + winner + ' you have won an ice cream sundae!')

#Set another variable named prompt to the text Would you like a cherry on top?
prompt = 'Would you like a cherry on top? '

#Set wants_cherry as input. User would be ask to give the input .
wants_cherry = input(prompt)

#Set a variable named order contains flavor (declared before as vanilla) and sundae.
order = flavor + ' sundae '

#Set up a condition that if user give input as yes,
#order variable will add with a cherry on top.
if (wants_cherry == 'yes'):
    order = order + ' with a cherry on top'

#Printing , One selected order(flavor and details) for winner’s (name) is coming right up.
print('One ' + order + ' for ' + winner +
' coming right up...')
