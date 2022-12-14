import json
from plotly.graph_objs import Bar, Layout
from plotly import offline



numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0]
filename = "populationbycountry.json"

with open(filename) as f:
    data = json.load(f)

for key in data:
    population = str(key['population'])
    leadingNum = population[0]
    if not leadingNum == '0':
        index = numList.index(leadingNum)
        frequency[index] += 1



data = [Bar(x=numList, y=frequency)]
x_axis_config = {'title': 'Possible Nums'}
y_axis_config = {'title': 'Frequency of Num'}
my_layout = Layout(title='Frequency of Possible Leading Nums for Country Population',
           xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='frequency.html')