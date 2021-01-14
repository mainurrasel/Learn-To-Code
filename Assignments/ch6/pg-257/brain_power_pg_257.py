text="""Rasel, Roni and Mehedi are cousins!
        They are 25, 26 and 15 yeras old."""
punctuations= """,!."""
no_punct=""
for char in text:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)
    

lyrics = 'I heard you on the wireless back in fifty two'
for char in lyrics:
    print(char)
