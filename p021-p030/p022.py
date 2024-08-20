# reading & sorting names
with open('p021-p030/names.txt', 'r') as file:
    names = [name.strip('"') for name in file.read().strip().split(',')]

names.sort()

# dictionary of alphabet scores
alphabet_scores = {chr(i): i - 64 for i in range(65, 91)}

# total of all the name scores
total = 0
score = 0
for i in range(len(names)):
    for j in range(len(names[i])):
        score += alphabet_scores[names[i][j]]
    total += score * (i + 1)
    score = 0
print(total)