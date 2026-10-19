import pandas as pd
import matplotlib.pyplot as plt

# Example portfolio notebook starter
df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "revenue": [1200, 1500, 1700, 1900]
})

print(df)

plt.plot(df["month"], df["revenue"])
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()