import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\mailt\\Desktop\\Diya\\DS_py\\Project\\Dataset.csv")


print("Dataset Overview: ")
print(df)


#2. Gender Gap in Schools: Investigating gender disparities in education, including number of boys schools, number of girls schools, and number of co-ed schools.
df = df[df["Location"] != "All India"]
gender_gap = df.groupby(["Location", "School Type"])["Total No of Schools"].sum().unstack(fill_value=0)
gender_gap

#A. Boys
plt.figure(figsize=(18, 8))
plt.plot(gender_gap.index, gender_gap["Boys"], label="Boys Schools", color="#4058ef")
plt.xticks(rotation=90)
plt.legend()
plt.ylabel("No. Of Schools")
plt.title("Boys Schools Across India")

#B. Girls
plt.figure(figsize=(18, 8))
plt.plot(gender_gap.index, gender_gap["Girls"], label="Girls Schools", color="#f577e4")
plt.xticks(rotation=90)
plt.legend()
plt.ylabel("No. Of Schools")
plt.title("Girls Schools Across India")

#C. Co-ed
plt.figure(figsize=(18, 8))
plt.plot(gender_gap.index, gender_gap["Co-Ed"], label="Co-Educational Schools", color="#34a154")
plt.xticks(rotation=90)
plt.legend()
plt.ylabel("No. Of Schools")
plt.title("Co-ed Schools Across India")

#D. Girls Vs Boys Vs Co-ed
plt.figure(figsize=(18, 8))
plt.plot(gender_gap.index, gender_gap["Boys"], label="Boys Schools", color="#4058ef")
plt.plot(gender_gap.index, gender_gap["Girls"], label="Girls Schools", color="#f577e4")
plt.plot(gender_gap.index, gender_gap["Co-Ed"], label="Co-Educational Schools", color="#34a154")
plt.xticks(rotation=90)
plt.legend()
plt.ylabel("No. Of Schools")
plt.title("Gender-wise Distribution Of Schools Across India")
plt.show()
