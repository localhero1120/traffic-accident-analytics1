import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("accidents.csv")
df["date"] = pd.to_datetime(df["date"])

# 1️⃣ Total accidents
print("Total Accidents:", len(df))

# 2️⃣ Accidents by location
location_counts = df["location"].value_counts()
location_counts.plot(kind="bar", title="Accidents by Location")
plt.savefig("location_chart.png")
plt.clf()

# 3️⃣ Accident type distribution
df["accident_type"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Accident Type Distribution"
)
plt.savefig("type_chart.png")
plt.clf()

# 4️⃣ Monthly accident trend
df["month"] = df["date"].dt.month
df.groupby("month").size().plot(
    kind="line",
    title="Monthly Accident Trend"
)
plt.savefig("monthly_trend.png")

print("Charts generated successfully macha 🔥")
