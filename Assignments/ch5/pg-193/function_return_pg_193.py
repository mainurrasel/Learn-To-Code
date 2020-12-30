#Check outputs
def get_bark(weight):
    if weight > 20:
        return 'WOOF WOOF'
    else:
        return 'woof woof'

#codies_bark = get_bark(40)
#print("Codie's bark is", codies_bark)
codies_bark = get_bark(20)
print(codies_bark)

def make_greeting(name):
    return 'Hi ' + name + '!'
x = make_greeting('Speedy')
print (x)

def compute(x, y):
    total = x + y
    if (total > 10):
        total = 10
    return total
#compute = compute(2,3)
#print(compute)
compute = compute(11,13)
print(compute)


def allow_access(person):
    if person == 'Dr Evil':
        answer = True
    else:
        answer = False
    return answer
#allow_access = allow_access('Codie')
#print(allow_access)
allow_access = allow_access('Dr Evil')
print(allow_access)


#inputs:
#get_bark(20)
#make_greeting('Speedy')
#compute(2, 3)
#compute(11, 3)
#allow_access('Codie')
#allow_access('Dr Evil')
