
# BASIC: 0 to 150:

for integers in range (0,151):
    print(integers)


# # MULTIPLES OF FIVE:

for multiples_of_Five in range (5,1001,5):
    print(multiples_of_Five)

# COUNTING THE DOJO WAY

for intergers in range (1,101):
    if intergers % 10 == 0:
        print("Coding Dojo")
    elif intergers % 5 == 0:
        print("Coding")
    else:
        print(intergers)


# WHOA, THAT SUCKER IS HUGE

sum = 0
for i in range (0,500001):
    sum = sum + i
    i += 1
print(sum)


# COUNTDOWN BY FOURS

for i in range (2018,0,-4):
    print(i)

# FLEXIBLE COUNTER

lowNum = 5
highNum = 50
mult = 7

for i in range (5,51):
    if i % mult == 0:
        print(i)