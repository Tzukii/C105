import csv
import pandas as pd
import plotly.express as px

with open("class1.csv", newline="") as f:
    read=csv.reader(f)
    fileData = list(read)

#remove header from csv

fileData.pop(0)

totalMarks = 0

totalEntries = len(fileData)

for marks in fileData:
    totalMarks += float(marks[1])

mean = totalMarks/totalEntries

print("This is the mean: "+str(mean))

df=pd.read_csv("class1.csv")

fig = px.scatter(df, x="Student Number", y="Marks")
fig.update_layout(shapes=[
    dict(
        type="line",
        y0=mean,
        y1=mean,
        x0=0,
        x1=totalEntries
    )
])

fig.update_yaxes(rangemode="tozero")

fig.show()