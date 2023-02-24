# A - Sum all the numbers up to line 631
rows = range(631)
total = 0
for row in rows:
    cols = range(row + 1)
    for col in cols:
        total = total + col + 1
print(total)

# B - What is term 76?
num = -1
den = 1
terms = range(76)
for i in terms:
    num = num + 2
    den = den * 2
print(num, den)

# C - Sum the first 2592 terms
total = 0
terms = range(2592)
for i in terms:
    total = total + i % 4
print(total)

# D - Sum all numbers from [1 - 148)
total = 0
terms = range(148)
for term in terms:
    total = total + term
print(total)

# Plus - Sum all odd numbers from [1 - 952]
total = 0
terms = range(1, 953, 2)
for term in terms:
    total = total + term
print(total)