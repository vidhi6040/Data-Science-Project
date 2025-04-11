import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\mailt\\Desktop\\Diya\\DS_py\\Project\\Dataset.csv")

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

#4. Infrastructure Analysis in Rural Areas: Focusing on the availability of school infrastructure in rural regions to uncover challenges faced in non-urban areas and support data-driven educational interventions.

rural_infra = df.groupby("Rural/Urban")[["Functional Drinking Water", "Functional Electricity", "Functional Toilet Facility", "Furniture", "Handwash", "Water Purifier"]].sum().T
rural_infra.plot(kind="bar", color=["#f1d2cd", "#e15e5e"])
plt.title("Infrastructure Comparison: Rural vs Urban Schools")
plt.ylabel("Number of Schools with Facility")
plt.xlabel("Infrastructure Type")
plt.xticks(rotation=45)
plt.legend(title="Location")
