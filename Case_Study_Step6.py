import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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

#################################################
# Step 5 : Split the dataset for traing and testing
#################################################

print(Border)
print("Step 5 : Split the dataset for traing and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y)

print("Dataset splitting activity done")

print("X : ",X.shape)
print("Y : ",Y.shape)

print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)

print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)

#################################################
# Step 6 : Build the model
#################################################

print(Border)
print("Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model gets created sucessfully")

#################################################
# Step 7 : Train the  model
#################################################

print(Border)
print("Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model train sucessfully")