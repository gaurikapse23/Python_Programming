# ==========================================
# Fake News Detection using Voting Classifier
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousFakeNewsPredictor():

    # =========================
    # 1. Load Dataset
    # =========================
    fake_df = pd.read_csv("fake.csv")
    true_df = pd.read_csv("true.csv")

    # Add labels
    fake_df['label'] = 0   # Fake
    true_df['label'] = 1   # Real

    # Combine datasets
    df = pd.concat([fake_df, true_df], axis=0)

    # =========================
    # 2. Data Preprocessing
    # =========================
    df = df[['text', 'label']]   # use text column
    df.dropna(inplace=True)

    print("First 5 rows:\n", df.head())
    print("\nDataset Info:\n")
    print(df.info())

    # =========================
    # 3. EDA
    # =========================
    sns.countplot(x='label', data=df)
    plt.title("Fake vs Real News Distribution")
    plt.show()

    # =========================
    # 4. Feature Extraction (TF-IDF)
    # =========================
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)

    X = tfidf.fit_transform(df['text'])
    y = df['label']

    # =========================
    # 5. Train-Test Split
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # =========================
    # 6. Model Training
    # =========================
    lr = LogisticRegression(max_iter=1000)
    dt = DecisionTreeClassifier()

    # Individual models
    lr.fit(X_train, y_train)
    dt.fit(X_train, y_train)

    # Voting Classifier
    voting_hard = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='hard'
    )

    voting_soft = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='soft'
    )

    voting_hard.fit(X_train, y_train)
    voting_soft.fit(X_train, y_train)

    # =========================
    # 7. Evaluation
    # =========================
    models = {
        "Logistic Regression": lr,
        "Decision Tree": dt,
        "Voting (Hard)": voting_hard,
        "Voting (Soft)": voting_soft
    }

    for name, model in models.items():
        print("\n======================")
        print("Model:", name)

        y_pred = model.predict(X_test)

        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

    # =========================
    # 8. Confusion Matrix Plot (Best Model)
    # =========================
    best_model = voting_soft   # usually best

    y_pred = best_model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    sns.heatmap(cm, annot=True, fmt='d')
    plt.title("Confusion Matrix (Best Model)")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # =========================
    # 9. Final Output
    # =========================
    sample_text = ["Breaking news: Government announces new policy"]

    sample_vector = tfidf.transform(sample_text)
    prediction = best_model.predict(sample_vector)

    if prediction[0] == 1:
        print("\nPrediction: REAL News")
    else:
        print("\nPrediction: FAKE News")

    # Save predictions
    final_pred = best_model.predict(X_test)

    output = pd.DataFrame({
        "Actual": y_test,
        "Predicted": final_pred
    })

    output.to_csv("fake_news_predictions.csv", index=False)

    print("\nPredictions saved to fake_news_predictions.csv")


# =========================
# Main Function
# =========================
def main():
    print("----- Fake News Detection System -----")
    MarvellousFakeNewsPredictor()


if __name__ == "__main__":
    main()