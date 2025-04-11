import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Reading data from csv file
df = pd.read_csv("C:\\Users\\mailt\\Desktop\\Diya\\DS_py\\Project\\Dataset.csv")


# Clean column names
df.columns = df.columns.str.strip().str.replace("_", "  ").str.replace("(", "").str.replace(")", "").str.replace(",", "").str.replace("’", "").str.replace("'", "").str.replace(".", "")


#DataSet
print("Dataset Overview: ")
print(df)


#Basic EDA Prints
print("Basic EDA prints: ")
print(df.describe())
print(df.info())
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.isnull().sum())


# Map school managements
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


