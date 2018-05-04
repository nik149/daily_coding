import random
def monteCarlo():
    numSims = input('number of simulations: ')

    pointsInsideCircle = 0
    totalPoints = numSims
    for i in range(0, numSims):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        #check if falls inside circle
        if(x*x + y*y <= 1):
            pointsInsideCircle += 1

    pi = 4.0 * float(pointsInsideCircle)/float(totalPoints)

    return pi

print monteCarlo()

