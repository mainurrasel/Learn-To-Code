def attribute(question, default):
    ask = question + '['+ default + ']?'
    answer = input(ask)
    if answer == "" :
        answer = default
    print("You chose", answer)

hair = attribute('What hair color', 'brown')
hair_length = attribute('What hair length', 'short')
eye = attribute('What eye color', 'blue')
gender = attribute('What gender', 'female')
glasses = attribute('Has glasses', 'no')
beard = attribute('Has beard', 'no')
