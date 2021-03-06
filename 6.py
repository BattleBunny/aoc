import re
f = open("6.txt")
lines = f.readlines()
coordinates = [re.findall("[\w']+", line) for line in lines] 
x = int(max(coordinates, key=lambda x:int(x[0]))[0])+1
y = int(max(coordinates, key=lambda x:int(x[1]))[1])+1
locations = [[[500,0] for j in range(x)] for i in range(y)]

for i in range(y):
    for j in range(x):
        for k in range(len(lines)):
            distance = abs(i-int(coordinates[k][0])) + abs(j-int(coordinates[k][1]))
            if distance == locations[i][j][0]:
                locations[i][j][0] == 0
            elif distance < locations[i][j][0]:
                locations[i][j][0] = distance
                locations[i][j][1] = k
scores = [0]*len(lines)

for i in range(y):
    for j in range(x):
        if locations[i][j][0] != 0:
            if (i == 0 or j == 0 or i == y-1 or j == x-1):
                scores[locations[i][j][1]] = -1
            elif scores[locations[i][j][1]] != -1:
                scores[locations[i][j][1]] += 1
            
print(sorted(scores))
print(max(scores))
