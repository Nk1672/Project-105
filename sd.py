import math
import csv

with open("sd.csv",newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    n = len(data)
    total = 0

    for i in data:
        total+=int(i)
    mean = total/n
    
    return mean

squareList = []

for a in data: 
    sub = int(a)-mean(data)
    sqr = sub**2
    squareList.append(sqr)

sum = 0
for x in squareList:
    sum+=x

result = sum/(len(data)-1)

sd = math.sqrt(result)

print("The standard deviation of this set is : ",sd)