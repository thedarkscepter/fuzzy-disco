import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff 

df = pd.read_csv('data.csv')

data = df['average'].tolist()

population_mean = statistics.mean(data)
sd = statistics.stdev(data)
print('mean is ', population_mean)
print('standard deviation is ', sd)
#fig = ff.create_distplot([data], ['average'], show_hist = False)
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
#for i in range(0,1000):
 #   random_index = random.randint(0,len(data))
 #   value = data[random_index]
#    dataset.append(value)

#mean1 = statistics.mean(dataset)
#sd1 = statistics.stdev(dataset)

#print('mean1 is ', mean)
#print('standard deviation1 ', sd)

#fig = ff.create_distplot([dataset], ['temp'], show_hist = False)
#fig.show()


def rand_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)

    mean1 = statistics.mean(dataset)

    return mean1 

def show_fig(mean_list):
    df = mean_list
    mean1 = statistics.mean[mean_list]
    print('mean of sampling distribution', mean1)
    fig = ff.create_distplot([dataset], ['average'], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = rand_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()