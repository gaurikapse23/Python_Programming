# ================================
# Diabetes Prediction - Single File
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousDiabetesPredictor():

    # ========================
    # 1. Load Dataset
    # ========================
    df = pd.read_csv("diabetes.csv")

    print("First 5 Rows:\n", df.head())
    print("\nDataset Info:\n")
    print(df.info())
    print("\nNull Values:\n", df.isnull().sum())
    print("\nStatistics:\n", df.describe())

    # ========================
    # 2. EDA Visualization
    # ========================
    sns.countplot(x='Outcome', data=df)
    plt.title("Outcome Distribution")
    plt.show()

    # ========================
    # 3. Data Preprocessing
    # ========================
    cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']

    for col in cols:
        df[col] = df[col].replace(0, df[col].median())

    # Features and Target
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # ========================
    # 4. Model Building
    # ========================
    lr = LogisticRegression()
    knn = KNeighborsClassifier(n_neighbors=5)
    dt = DecisionTreeClassifier()

    lr.fit(X_train, y_train)
    knn.fit(X_train, y_train)
    dt.fit(X_train, y_train)

    models = {
        "Logistic Regression": lr,
        "KNN": knn,
        "Decision Tree": dt
    }

    # ========================
    # 5. Evaluation
    # ========================
    best_model = None
    best_accuracy = 0

    for name, model in models.items():
        print("\n======================")
        print("Model:", name)

        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print("Accuracy:", acc)

        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

        if acc > best_accuracy:
            best_accuracy = acc
            best_model = model

    # ========================
    # 6. Confusion Matrix Plot
    # ========================
    y_pred = best_model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)

    sns.heatmap(cm, annot=True, fmt='d')
    plt.title("Best Model Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # ========================
    # 7. Final Prediction
    # ========================
    final_pred = best_model.predict(X_test)

    print("\nBest Model Accuracy:", best_accuracy)
    print("Predictions:\n", final_pred)

    # Save output
    output = pd.DataFrame({
        "Actual": y_test,
        "Predicted": final_pred
    })

    output.to_csv("diabetes_predictions.csv", index=False)

    print("\nPredictions saved to diabetes_predictions.csv")


# ========================
# Main Function
# ========================
def main():
    print("----- Diabetes Prediction System -----")
    MarvellousDiabetesPredictor()


if __name__ == "__main__":
    main()