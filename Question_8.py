import pandas as pd

data = {
"A": [1, 2, 2, 1],
"B": [3.1, 4.2, 1.5, 6.3],
"C": [800, 150, 400, 210]
}

df = pd.DataFrame(data) # create Dataframe
df["D (Total)"] = df["A"]+df["B"]+df["C"] # new column derived from existing columns

print(df) # prints final dataframe