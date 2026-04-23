import matplotlib.pyplot as plt
import pandas as pd 
df =  pd.read_csv("report.csv")
print(df)
names= df["Name"].tolist()
values = df["Average"]
plt.pie(values, labels=names, autopct="%1.1f%%")
plt.title("Average Marks Report")       
plt.show()