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

#5.	Impact of Private vs. Government Schools on Students: Comparing the infrastructure provided by private and government schools to understand its potential influence on students’ learning environment and development.

infra_comparison = df.groupby("School_Type_Grouped")[["Functional Drinking Water","Functional Electricity","Functional Toilet Facility","Furniture","Handwash","Water Purifier"
]].sum().T
infra_comparison.plot(kind="bar")
plt.title("Infrastructure Facilities: Government vs Private Schools")
plt.ylabel("Number of Schools with Functional Facility")
plt.xlabel("Infrastructure Type")
plt.xticks(rotation=45)
plt.legend(title="School Type")
plt.tight_layout()
