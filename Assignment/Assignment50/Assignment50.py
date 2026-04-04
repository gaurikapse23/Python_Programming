# ==========================================
# Bank Term Deposit Prediction - Single Code
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

def MarvellousBankPredictor():

    # =========================
    # 1. Load Dataset
    # =========================
    df = pd.read_csv("bank.csv", sep=';')   # UCI dataset uses ';'

    print("First 5 Rows:\n", df.head())
    print("\nInfo:\n")
    print(df.info())
    print("\nNull Values:\n", df.isnull().sum())

    # =========================
    # Handle 'unknown' values
    # =========================
    df.replace("unknown", np.nan, inplace=True)
    df.fillna(method='ffill', inplace=True)

    # =========================
    # Target Encoding (yes/no → 1/0)
    # =========================
    df['y'] = df['y'].map({'yes':1, 'no':0})

    # =========================
    # 2. EDA
    # =========================
    sns.countplot(x='y', data=df)
    plt.title("Subscription Distribution")
    plt.show()

    print("\nStatistics:\n", df.describe())

    # =========================
    # 3. Encoding Categorical Data
    # =========================
    le = LabelEncoder()

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = le.fit_transform(df[col])

    # =========================
    # 4. Split Data
    # =========================
    X = df.drop('y', axis=1)
    y = df['y']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # =========================
    # 5. Scaling
    # =========================
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # =========================
    # 6. Model Training
    # =========================
    lr = LogisticRegression()
    knn = KNeighborsClassifier(n_neighbors=5)
    rf = RandomForestClassifier()

    lr.fit(X_train, y_train)
    knn.fit(X_train, y_train)
    rf.fit(X_train, y_train)

    models = {
        "Logistic Regression": lr,
        "KNN": knn,
        "Random Forest": rf
    }

    # =========================
    # 7. Evaluation
    # =========================
    best_model = None
    best_acc = 0

    for name, model in models.items():
        print("\n======================")
        print("Model:", name)

        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print("Accuracy:", acc)

        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

        # ROC-AUC
        y_prob = model.predict_proba(X_test)[:,1]
        roc = roc_auc_score(y_test, y_prob)
        print("ROC-AUC Score:", roc)

        if acc > best_acc:
            best_acc = acc
            best_model = model

    # =========================
    # 8. Confusion Matrix Plot
    # =========================
    y_pred = best_model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    sns.heatmap(cm, annot=True, fmt='d')
    plt.title("Best Model Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # =========================
    # 9. ROC Curve
    # =========================
    y_prob = best_model.predict_proba(X_test)[:,1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)

    plt.plot(fpr, tpr)
    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.show()

    # =========================
    # 10. Final Output
    # =========================
    final_pred = best_model.predict(X_test)

    print("\nBest Model Accuracy:", best_acc)
    print("Predictions:\n", final_pred)

    # Save to CSV
    output = pd.DataFrame({
        "Actual": y_test,
        "Predicted": final_pred
    })

    output.to_csv("bank_predictions.csv", index=False)

    print("\nPredictions saved to bank_predictions.csv")


# =========================
# Main Function
# =========================
def main():
    print("----- Bank Subscription Prediction -----")
    MarvellousBankPredictor()


if __name__ == "__main__":
    main()