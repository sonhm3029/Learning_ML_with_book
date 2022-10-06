import pandas as pd
import numpy as np


s = pd.Series([1, 3, 4, np.nan, 6, 8])
print(s)

dates = pd.date_range(start="01/01/2022", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df)
print(df.dtypes)
print(df.head(1))
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.describe())
print(df.sort_index())
print(df.sort_values(by='B'))

# Selection
print(df['A'])
print(df[0:3])
print(df["20220101":"20220103"])

# Selection by label
print(df.loc[dates[0]])
print(df.loc[:, ["A", "B"]])
print(df.loc["20220101":"20220103", ["A", "B"]])
print(df.loc[dates[0], "A"])
print(df.at[dates[0], "A"])

# Select by Position
print(df.iloc[3])
print(df.iloc[3:5, 0:2])
print(df.iloc[[1,2,3], [0,2]])
print(df.iloc[1:3, :])
print(df.iloc[:, 1:3])
print(df.iloc[1,1])
print(df.iat[1,1])

# Boolean indexing
print(df[df["A"] > 0])
print(df[df > 0])

df["E"] = ["one", "one", "two", "three", "four", "three"]
print(df[df["E"].isin(["two", "four"])])

# Setting
s1 = pd.Series(list(range(1,7)), index=pd.date_range("20130102", periods=6))
print(s1)
df["F"] = s1

# Setting value by label
df.at[dates[0], "A"] = 0
df.iat[0, 1] = 0
df.loc[:,"D"] = np.array([5] * len(df))
print(df)


# Setting by aplly where operation
df2 = df.copy()



