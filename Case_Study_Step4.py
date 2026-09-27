import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*40

#################################################
# Step 1 : Load The Dataset
#################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded sucessfully")

print("Initial entries from dataset are : ")
print(df.head())

#################################################
# Step 2 : Data Analysis (EDA)
#################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Missing values per column : ")
print(df.isnull().sum())

print("Class distribution (species count) : ")
print(df["species"].value_counts())

print("Statistical report of dataset : ")
print(df.describe())

#################################################
# Step 3 : Decide Independent & Dependent Variables
#################################################

print(Border)
print("Step 3 : Decide Independent & Dependent Variables")
print(Border)

# X : Independent variable / Features
# Y : Dependent variable / Lables

feature_col = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]

X = df[feature_col]
Y = df["species"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

#################################################
# Step 4 : Visualization of dataset
#################################################

print(Border)
print("Visualization of dataset")
print(Border)

# Scatter plot

plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["sepal length (cm)"], temp["sepal width (cm)"], label = sp)

plt.title("Marvellous iris case study")

plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")

plt.legend()
plt.grid()
plt.show()


