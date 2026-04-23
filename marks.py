import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marks.csv")
print(df)

plt.bar(df["name"], df["marks"])
plt.xlabel("Name")
plt.ylabel("Marks")
plt.title("Student Marks Graph")
plt.show()