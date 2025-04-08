import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\mailt\\Desktop\\Diya\\DS_py\\Project\\Dataset.csv")


print("Dataset Overview: ")
print(df)


print("Basic EDA prints: ")
print(df.describe())
print(df.info())
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.isnull().sum())
