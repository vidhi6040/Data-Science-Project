import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\mailt\\Desktop\\Diya\\DS_py\\Project\\Dataset.csv")


print("Dataset Overview: ")
print(df)

management_map = {
    # Private
    "Private Unaided (Recognized)": "Private",
    "Unrecognized": "Private",
    "Madarsa recognized (by Wakf board/Madarsa Board)": "Private",
    "Madarsa unrecognized": "Private",
    
    # Government
    "Department of Education": "Government",
    "Government Aided": "Government",
    "Tribal Welfare Department": "Government",
    "Local body": "Government",
    "Social welfare Department": "Government",
    "Other Govt. managed schools": "Government",
    "Kendriya Vidyalaya / Central School": "Government",
    "Jawahar Navodaya Vidyalaya": "Government",
    "Other Central Govt. Schools": "Government",
    "Railway School": "Government",
    "Sainik School": "Government",
    "Ministry of Labor": "Government",
    "Central Tibetan School": "Government"
}
df["School_Type_Grouped"] = df["School Management"].map(management_map)
df["School_Type_Grouped"]


#2. Access to Educational Technology: Evaluating the availability of computers and internet in Indian schools across different states, school types, and management to understand digital readiness.
#A. Computer
df_B = df[df["Location"] != "All India"]
computer = df_B.groupby("Location")[["Computer Available", "Total No. of Schools"]].sum()
computer

computer["Computers Available (in %)"] = (computer["Computer Available"]/computer["Total No. of Schools"])*100
computer["Computers Available (in %)"]

plt.figure(figsize=(18, 24))
sns.heatmap(computer[["Computers Available (in %)"]], annot=True, cmap="coolwarm", linewidths=1.5)
plt.title("Heatmap of Computer Availability in Schools by State")
df_B = df[df["Location"] != "All India"]

#B. Internet
internet = df_B.groupby("Location")[["Internet", "Total No. of Schools"]].sum()
internet
internet["Internet Available (in %)"] = (internet["Internet"]/internet["Total No. of Schools"])*100
internet["Internet Available (in %)"]
plt.figure(figsize=(18, 24))
sns.heatmap(internet[["Internet Available (in %)"]], annot=True, cmap="coolwarm", linewidths=1.5)
plt.title("Heatmap of Internet Available in Schools by State")

#C. Government Vs Private
tech_comparison = df.groupby("School_Type_Grouped")[["Computer Available", "Internet"]].sum().T
tech_comparison
tech_comparison.loc["Computer Available"].plot(
    kind="pie", 
    autopct='%1.1f%%', 
    colors=["#34a154", "#3831a7"], 
    figsize=(5,5),
    title="Distribution of Computer Access: Government vs Private Schools"
)

