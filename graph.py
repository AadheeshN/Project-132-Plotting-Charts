import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Data
data = []
with open("final_data.csv", 'r') as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    data.append(row)

headers = data[0]
star_data = data[1:]

name = []
distance = []
mass = []
radius = []
gravity = []

for star_data in star_data:
    name.append(star_data[1])
    distance.append(star_data[2])
    mass.append(star_data[3])
    radius.append(star_data[4])

fig1 = px.scatter(x = mass, y = radius, title = "Mass and Radius")
fig1.show()
