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


#3. Access to Educational Technology: Evaluating the availability of computers and internet in Indian schools across different states, school types, and management to understand digital readiness.
#A. Computer
df_B = df[df["Location"] != "All India"]
computer = df_B.groupby("Location")[["Computer Available", "Total No. of Schools"]].sum()
computer
computer["Computers Available (in %)"] = (computer["Computer Available"]/computer["Total No. of Schools"])*100
computer["Computers Available (in %)"]
plt.figure(figsize=(18, 10))
computer["Computers Available (in %)"].plot(kind='bar', color="#8e468a")
plt.title("Computer Availability in Schools by State")
plt.xlabel("State")
plt.ylabel("Computers Available (in %)")
plt.xticks(rotation=90)

#B. Internet
internet = df_B.groupby("Location")[["Internet", "Total No. of Schools"]].sum()
internet
internet["Internet Available (in %)"] = (internet["Internet"]/internet["Total No. of Schools"])*100
internet["Internet Available (in %)"]
plt.figure(figsize=(18, 10))
internet["Internet Available (in %)"].plot(kind='bar', color="pink")
plt.title("Internet Availability in Schools by State")
plt.xlabel("State")
plt.ylabel("Computers Available (in %)")
plt.xticks(rotation=90)

#C. Government Vs Private
tech_comparison = df.groupby("School_Type_Grouped")[["Computer Available", "Internet"]].sum().T
tech_comparison
tech_cols = ["Computer Available", "Internet"]
tech_comparison = df.groupby("School_Type_Grouped")[tech_cols].sum().T
tech_comparison.plot(kind="bar", color=["#8e468a", "pink"])
plt.title("Access to Computers and Internet: Government vs Private Schools")
plt.ylabel("Number of Schools with Access")
plt.xlabel("Technology Type")
plt.xticks(rotation=0)
plt.legend(title="School Type")
plt.tight_layout()
plt.show()

