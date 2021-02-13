import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff 

df = pd.read_csv('data.csv')

data = df['temp'].tolist()

population_mean = statistics.mean(data)
sd = statistics.stdev(data)
print('mean is ', population_mean)
print('standard deviation is ', sd)
#fig = ff.create_distplot([data], ['temp'], show_hist = False)
#fig.show()
dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
sd = statistics.stdev(dataset)

print('mean is ', mean)
print('standard deviation', sd)

for i in range(0,1000):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean1 = statistics.mean(dataset)
sd1 = statistics.stdev(dataset)

print('mean1 is ', mean)
print('standard deviation1 ', sd)

fig = ff.create_distplot([dataset], ['temp'], show_hist = False)
fig.show()