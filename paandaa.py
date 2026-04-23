import pandas
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)

import pandas as pd
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])

import pandas as pd
data = {
    "name":["A","B","C","D","E","F","G","H","I","J"],
    "marks":[85, 90, 78, 92, 88, 95, 80, 91, 89, 94]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[6])
print(df.loc[4])