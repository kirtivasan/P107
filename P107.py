import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

student_df = df.loc[df['student_id']=='TRL_abc']

print(student_df.groupby("level")["attempt"].mean())


fig = px.scatter(df,x = "student_id", y = "level",size = "attempt",color = "level",size_max = 60)

fig.show()

