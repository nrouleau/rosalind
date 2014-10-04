months = 92
life = 18

rabbitlist = [1]
rabbitlistold = [1]
for i in range(life-1):
    rabbitlist.append(0)
    rabbitlistold.append(0)

for i in range(months-1):
    newrabbits = 0
    
    for j in range(1, life):
        newrabbits += rabbitlistold[j];

    for j in range(1, life):
        rabbitlist[j] = rabbitlistold[j-1]
    rabbitlist[0] = newrabbits

    for j in range(0,life):
        rabbitlistold[j] = rabbitlist[j]

sumR = 0
for rabbits in rabbitlist:
    sumR += rabbits

print sumR
