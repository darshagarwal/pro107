import pandas as pd
import csv
import plotly.express as px

df= pd.read_csv("/Volumes/NEW VOLUME/pro107/data.csv")

mean_student_level= df.groupby("level") ["attempt"].mean()

fig= px.scatter(df,x=mean_student_level,y=['Level 1','Level 2','Level 3','Level 4'],color=mean_student_level,size_max=300)
fig.show()