import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("/Users/raama/Documents/White hat jr./python/p110/data.csv")
data = df["average"].tolist()

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([data],["average"],show_hist = False)
    fig.add_trace(go.Scatter(x=[mean, mean], y = [0,1], mode = "lines", name="MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_means(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()

average_mean = statistics.mean(data)
print("Average mean:", average_mean)

def standard_deviation():
    mean_list=[]
    for i in range(0, 1000):
        set_of_means = random_set_of_means(100)
        mean_list.append(set_of_means)
    
    std_deviation = statistics.stdev(mean_list)
    print("Standard Deviation of Sample:", std_deviation)

standard_deviation()