"""
Diabates Predictor 
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("diabetes.csv")

    print(df.head())

    print(df.info())

    print(df.isnull().sum())

    print(df.describe())

    plt.figure(figsize=(5,4))
    plt.hist(df["Outcome"], bins=2, edgecolor='black')
    plt.title(" Distribution of Outcome")
    plt.xlabel("Outcome")
    plt.ylabel("Frequency")
    plt.show()

    df.boxplot(figsize=(12,6))
    plt.title("Boxplot for Outlier Detection")
    plt.show()

    zero_columns = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    for col in zero_columns:
        df[col] = df[col].replace(0, df[col].median())

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    #Logistic Regression
    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # KNN
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    model_pred = model.predict(X_test)

    #Decision Tree
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    model_pred = model.predict(X_test)

    print("\n----------------------- LOGISTIC REGRESSION -------------------")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    print("\n----------------------- KNN -----------------------")
    print("Accuracy:", accuracy_score(y_test, model_pred))
    print(classification_report(y_test, model_pred))

    print("\n----------------------- DECISION TREE -----------------------")
    print("Accuracy:", accuracy_score(y_test, model_pred))
    print(classification_report(y_test, model_pred))


    # Confusion matrix visualization with Logistic Regression
    Con_Mat = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6,5))
    sns.heatmap(Con_Mat, annot=True, cmap="Blues", fmt="d",
                xticklabels=["Non-Diabetic", "Diabetic"],
                yticklabels=["Non-Diabetic", "Diabetic"])

    plt.title("Confusion Matrix - Logistic Regression")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()


    output_df = pd.DataFrame({
        "Actual Outcome": y_test.values,
        "Predicted Outcome": y_pred
        })

    print("\nFINAL PREDICTIONS:")
    print(output_df.head())

    output_df.to_csv("Diabetes_Predictions.csv", index=False)
    print("\nPredictions saved to Diabetes_Predictions.csv")


if __name__ == "__main__":
    main()