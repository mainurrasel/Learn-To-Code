#calling function
def hook_fish():
    print('I got a fish!')
def wait():
    print('waiting...')
x=input('enter function:')
if(x=='hook fish'):
    hook_fish()
else:
    wait()
