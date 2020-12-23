scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
i = 0
length = len(scores)
print("Length of the list is:",length,("\n"))
while i < length:
    bubble_string = 'Bubble solution #' + str(i)
    print(bubble_string, 'score:', scores[i])
    i = i + 1
