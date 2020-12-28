scores = [60, 50, 60, 58, 54, 54,
58, 50, 52, 54, 48, 69,
34, 55, 51, 52, 44, 51,
69, 64, 66, 55, 52, 61,
46, 31, 57, 52, 44, 18,
41, 53, 55, 61, 51, 44]
high_score = 0
length = len(scores)
#computing scores with index number
for i in range(length):
    print('Bubble solution #' + str(i), 'score:', scores[i])
    
#computing highest score
    if scores[i] > high_score:
        high_score = scores[i]
print('Bubbles tests:', length)
print('Highest bubble score:', high_score)

#computing best solution index
best_solutions = []
for i in range(length):
    if high_score == scores[i]:
        best_solutions.append(i)
print('Solutions with the highest score:', best_solutions)

#computing lowest score
lowest_score = 100
for i in range(length):
    if scores[i] < lowest_score:
        lowest_score = scores[i]
print('Lowest bubble score:', lowest_score)

#computing worst solution index
worst_solutions = []
for i in range(length):
    if lowest_score == scores[i]:
        worst_solutions.append(i)
print('Solutions with the lowest score:', worst_solutions)
