#creating function
#if we give one extra comma, function accept that
#def bark(name, weight,):
def bark(name, weight,):
    if weight > 20:
        print(name, 'says WOOF WOOF',   )
    else:
        print(name, 'says woof woof',   )
#calling function
bark('Codie', 40,)
bark('Sparky', 9,)
bark('Jackson', 12,)
bark('Fido', 65,)
#TypeError: bark() takes 2 positional arguments but 3 were given
#bark('Fido',60,50)

#extra comma in list
A=['a','b',]
print(A,)
