import pandas as pd
import random
from datetime import datetime, timedelta

locations = ["Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi"]
accident_types = ["Collision", "Over Speed", "Hit and Run", "Skid", "Other"]

data = []

for i in range(1200):
    record = {
        "date": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d"),
        "location": random.choice(locations),
        "accident_type": random.choice(accident_types),
        "vehicles_involved": random.randint(1, 4),
        "injuries": random.randint(0, 5),
        "deaths": random.randint(0, 2)
    }
    data.append(record)

df = pd.DataFrame(data)
df.to_csv("accidents.csv", index=False)

print("Dummy accident dataset created macha ✅")
