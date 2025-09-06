import pandas as pd
import numpy as np

df = pd.DataFrame({
    "age": [25, 30, 35],
    "income": [50000, 60000, 70000]
})

# Old (removed)
# arr = df.as_matrix()

# Correct new usage
arr1 = df.values
arr2 = df.to_numpy()

print(arr1)
print(arr2)
