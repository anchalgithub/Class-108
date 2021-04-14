import csv
import pandas as pd
import plotly.figure_factory as ff
df = pd.read_csv("data.csv")
fig=ff.create_distplot([df["weight"].tolist()],["Weight"],show_hist=False)
fig.show()