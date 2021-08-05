import csv
import math

with open("data.csv", newline="") as f:
    read=csv.reader(f)
    fileData = list(read)

#remove header from csv

data = fileData.pop(0)

#mean

def mean(data):
    n=len(data)
    total = 0
    for x in data:
        total +=int(x)

    mean = total/n
    return(mean)

#squaring and getting the values
squaredList =[]

for number in data:
    a = int(number) - mean(data)

    a = a**2

    squaredList.append(a)

#Getting the sum
sum=0

for i in squaredList:
    sum = sum + i

#dividing the sum by total values - 1

result = sum/(len(data)-1)

#getting the standard deviation
standardDev = math.sqrt(result)

print("This is the Standard Deviation: " +str(standardDev))