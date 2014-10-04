clicks = 5
multiplier = 3

w1 = 0
w2 = 1

for i in range(clicks-1):
    w1, w2 = w2, w1*multiplier + w2 
 
print str(w2)
