import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/deathsbystateovertime.json'

with open(filename) as f:
    all_eq_data = json.load(f)

    print (all_eq_data)