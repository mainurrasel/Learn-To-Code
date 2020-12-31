#Steal unsuccessful
#Cause: in (steal)function , (balance)parameter is a shadow param,
#When the function called , Criminal actually called the shadow param and money amount 1250
#But this balance is not that amount of bank balance which is declared as global on top
#So the bank balance would remain same
#Criminal also turn off camera by global in the function,but he turns on again after return function.
#Ultimately the camera remains off.
balance = 10500
camera_on = True

def steal(balance, amount):
    global camera_on
    camera_on = False
    if (amount < balance):
        balance = balance - amount
    return amount
    camera_on = True
    
proceeds = steal(balance, 1250)
print('Criminal: you stole :', proceeds)
#print('New bank balance is :', balance)
print("Camera status:", camera_on)
print()

#Steal successful
balance = 10500
camera_on = True

def steal(money, amount):
    global camera_on
    camera_on = False
    global balance
    if (amount < balance):
        balance = balance - amount
    camera_on = True
    return amount
    
proceeds = steal(balance, 1250)
print('Criminal: you stole :', proceeds)
#print('New bank balance is :', balance)
print("Camera status:", camera_on)
