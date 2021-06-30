import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data2.csv")
gb = df.groupby(["student_id","level"] ,as_index=False)["attempt"].mean()
fig = px.scatter(gb, x = "student_id", y = "level", size = "attempt",size_max=30, color = "attempt")
fig.show()
