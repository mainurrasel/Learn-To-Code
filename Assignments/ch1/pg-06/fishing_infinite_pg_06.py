#Fishing
def hook_fish():
    print('I got a fish!')
def wait():
    print('waiting...')
print('Get worm')
print('Put worm on hook')
print('Throw in lure')


while True:
    response = input('Is bobber underwater? ')
    if response == 'yes':
        is_moving=True
        print('I got a bite!')
        hook_fish()
    else:
        wait()
#It's an infinite loop.While loop is not ending.
#So, the system will keep asking to user.
