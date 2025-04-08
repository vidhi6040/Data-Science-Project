import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\mailt\\Desktop\\Diya\\DS_py\\Project\\Dataset.csv")

#1.	Evaluating Basic Facility Access in Schools Across India: Analyze the availability of essential school facilities such as drinking water, toilets, handwashing stations, electricity, and furniture to assess the quality of basic learning environments across different regions and school types.
#A. Drinking Water
drinking_water = df.groupby("Location")[["Functional Drinking Water", "Total No. of Schools"]].sum()
print(drinking_water)
drinking_water["Drinking Water (in %)"] = (drinking_water["Functional Drinking Water"]/drinking_water["Total No. of Schools"])*100
print(drinking_water["Drinking Water (in %)"])
plt.figure(figsize = (18,8))
plt.bar(drinking_water.index, drinking_water["Drinking Water (in %)"], color="#65a2d7")
plt.xticks(rotation=90)
plt.ylabel("Percentage of Schools with Functional Drinking Water")
plt.title("Functional Drinking Water Access in Schools Across Indian States")

#B. Toilet
electricity = df.groupby("Location")[["Functional Electricity", "Total No. of Schools"]].sum()
electricityelectricity["Electricity (in %)"] = (electricity["Functional Electricity"]/electricity["Total No. of Schools"])*100
electricity["Electricity (in %)"]
plt.figure(figsize=(18,8))
plt.bar(electricity.index, electricity["Electricity (in %)"], color="#34a154")
plt.xticks(rotation=90)
plt.ylabel("Percentage of Schools with Functional Electricity")
plt.title("Functional Electricity Access in Schools Across Indian States")

#C. Furniture
furniture = df.groupby("Location")[["Furniture", "Total No. of Schools"]].sum()
furniturefurniture["Furnitures Available (in %)"] = (furniture["Furniture"]/furniture["Total No. of Schools"])*100
furniture["Furnitures Available (in %)"]
plt.figure(figsize=(18,8))
plt.bar(furniture.index, furniture["Furnitures Available (in %)"], color="#ef4b40")
plt.xticks(rotation=90)
plt.ylabel("Percentage of Schools with Furnitures")
plt.title("Furnitures Available in Schools Across Indian States")

#D. Handwash
handwash = df.groupby("Location")[["Handwash", "Total No. of Schools"]].sum()
handwash
handwash["Handwash (in %)"] = (handwash["Handwash"]/handwash["Total No. of Schools"])*100
handwash["Handwash (in %)"]
plt.figure(figsize=(18,8))
plt.bar(handwash.index, handwash["Handwash (in %)"], color="#8e468a")
plt.xticks(rotation=90)
plt.ylabel("Percentage of Schools with Handwashing Station")
plt.title("Handwashing Station Available in Schools Across Indian States")

#E. Water Purifier
water_purifier = df.groupby("Location")[["Water Purifier", "Total No. of Schools"]].sum()
water_purifier
water_purifier["Water Purifier (in %)"] = (water_purifier["Water Purifier"]/water_purifier["Total No. of Schools"])*100
water_purifier["Water Purifier (in %)"]
plt.figure(figsize=(18,8))
plt.bar(water_purifier.index, water_purifier["Water Purifier (in %)"], color="#f5901e")
plt.xticks(rotation=90)
plt.ylabel("Percentage of Schools with Water Purifier")
plt.title("Water Purifiers Available in Schools Across Indian States")

#F. Toilet
toilet = df.groupby("Location")[["Functional Toilet Facility", "Total No. of Schools"]].sum()
toilet
toilet["Toilets Available (in %)"] = (toilet["Functional Toilet Facility"]/toilet["Total No. of Schools"])*100
toilet["Toilets Available (in %)"]
plt.figure(figsize=(18,8))
plt.bar(toilet.index, toilet["Toilets Available (in %)"], color="#f577e4")
plt.xticks(rotation=90)
plt.ylabel("Percentage of Schools with Toilets Available")
plt.title("Toilet Access in Schools Across Indian States")
