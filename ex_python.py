import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# create lil dataframe
df = pd.DataFrame({
    "x": np.arange(10),
    "y": np.random.randn(10).cumsum()
})

# export dataframe
df.to_csv("demo_data_py.csv", index=False)

# make & save plot
plt.figure(figsize=(6,4))
plt.plot(df["x"], df["y"], marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Demo Plot")
plt.tight_layout()
plt.savefig("demo_plot.png")
plt.close()