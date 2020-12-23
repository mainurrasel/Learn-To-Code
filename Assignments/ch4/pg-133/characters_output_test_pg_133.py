characters = ['w','a', 's', 'i', 't', 'a', 'r']
#characters = ['b','a', 't']
#if we write two new varialbles, Shell will execute the last one.
#Empty string
output = ''
length = len(characters)
i = 0
#condition start ->forward
while (i < length):
    output = output + characters[i]
    i = i + 1
#condition end
    
#Reset value
length = length * -1
i = -2
#Another condition start <- backward 
while (i >= length):
    output = output + characters[i]
    i = i - 1
print(output)
