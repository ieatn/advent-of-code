x = [line.strip() for line in open('input.txt')]
score = 0
for i in x:
    op, me = i.split()
    print(me, op)
    score += {'X': 0, 'Y': 3, 'Z': 6}[me]
    score += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
                ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
                ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
                }[(op, me)]
print(score)
