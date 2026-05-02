import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("sales.csv")
print(df) 
daily = df.groupby("date")["sales"].sum()
print("\nDaily Sales:\n", daily)  
daily.plot(title="Sales Trend")  
plt.xlabel("Date"); plt.ylabel("Sales")
plt.show()