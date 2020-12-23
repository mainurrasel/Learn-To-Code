#We can fix range and start our for loop.
'''
for i in range(5):
    print('Iterating through', i)
'''
#printing the index of each component of the list.

smoothies = ['coconut',
             'strawberry',
             'banana',
             'tropical',
             'acai berry']    
length = len(smoothies)
for i in range(length):
    print('Smoothie #', i, smoothies[i])

