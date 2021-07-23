import random
from matplotlib import pyplot as plt


def random_walk(n, pathCounter, firstPathX, firstPathY, secondPathX, secondPathY, thirdPathX, thirdPathY, fourthPathX, fourthPathY):
    x = 0
    y = 0

    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1

        if pathCounter == 0:
            firstPathX.append(x)
            firstPathY.append(y)
        elif pathCounter == 1:
            secondPathX.append(x)
            secondPathY.append(y)
        elif pathCounter == 2:
            thirdPathX.append(x)
            thirdPathY.append(y)
        elif pathCounter == 3:
            fourthPathX.append(x)
            fourthPathY.append(y)
        else:
            continue

    return x, y


distances = list()
firstPathX = [0]
firstPathY = [0]
secondPathX = [0]
secondPathY = [0]
thirdPathX = [0]
thirdPathY = [0]
fourthPathX = [0]
fourthPathY = [0]
pathCounter = 0
distanceSum = 0

for i in range(10000):
    walk = random_walk(1000, pathCounter, firstPathX, firstPathY, secondPathX, secondPathY, thirdPathX, thirdPathY, fourthPathX, fourthPathY)
    pathCounter = pathCounter + 1
    distances.append(abs(walk[0]) + abs(walk[1]))

for distance in distances:
    distanceSum = distanceSum + distance

print("Average Distance: ", distanceSum / len(distances), "units")

plt.plot(firstPathX, firstPathY, secondPathX, secondPathY, thirdPathX, thirdPathY, fourthPathX, fourthPathY)
plt.title('Random Paths')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
