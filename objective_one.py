import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\mailt\\Desktop\\Diya\\DS_py\\Project\\Dataset.csv")

#1.	Evaluating Basic Facility Access in Schools Across India: Analyze the availability of essential school facilities such as drinking water, toilets, handwashing stations, electricity, and furniture to assess the quality of basic learning environments across different regions and school types.
state_facility = df.groupby("Location")[["Functional Drinking Water","Functional Electricity","Functional Toilet Facility","Furniture","Handwash","Water Purifier"]].sum()
plt.figure(figsize=(14, 10))
sns.heatmap(state_facility, annot=False, cmap="Blues", linewidths=0.5)
plt.title("Basic School Facilities Across States")
plt.xlabel("Facilities")
plt.ylabel("State")
plt.tight_layout()
