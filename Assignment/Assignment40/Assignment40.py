# -------------------------------------------------------------
# Student Performance ML - Advanced Tasks Solution
# -------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix

# -------------------------------------------------------------
# Load Dataset
# -------------------------------------------------------------
df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# =============================================================
# 1. Feature Importance
# =============================================================
print("\nFeature Importances:")
importance = pd.Series(model.feature_importances_, index=X.columns)
print(importance.sort_values(ascending=False))

print("\nMost Important Feature:", importance.idxmax())
print("Least Important Feature:", importance.idxmin())

# =============================================================
# 2. Remove SleepHours column
# =============================================================
X2 = df.drop(["FinalResult", "SleepHours"], axis=1)
y2 = df["FinalResult"]

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y2, test_size=0.3, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X2_train, y2_train)

acc_without_sleep = accuracy_score(y2_test, model2.predict(X2_test))
print("\nAccuracy without SleepHours:", round(acc_without_sleep * 100, 2), "%")

# =============================================================
# 3. Train model using only StudyHours & Attendance
# =============================================================
X_small = df[["StudyHours", "Attendance"]]
y_small = df["FinalResult"]

Xs_train, Xs_test, ys_train, ys_test = train_test_split(
    X_small, y_small, test_size=0.3, random_state=42
)

model_small = DecisionTreeClassifier(random_state=42)
model_small.fit(Xs_train, ys_train)

acc_small = accuracy_score(ys_test, model_small.predict(Xs_test))
print("\nAccuracy with 2 Features:", round(acc_small * 100, 2), "%")

# =============================================================
# 4. Predict 5 New Students
# =============================================================
new_students = pd.DataFrame({
    "StudyHours": [6, 2, 8, 4, 7],
    "Attendance": [85, 60, 90, 70, 95],
    "PreviousScore": [66, 45, 88, 55, 92],
    "AssignmentsCompleted": [7, 3, 9, 5, 10],
    "SleepHours": [7, 6, 8, 5, 7]
})

predictions = model.predict(new_students)

print("\nPredictions for 5 New Students:")
for i, p in enumerate(predictions):
    result = "PASS" if p == 1 else "FAIL"
    print(f"Student {i+1}: {result}")

# =============================================================
# 5. Manual Accuracy Calculation
# =============================================================
correct = np.sum(y_test.values == y_pred)
manual_accuracy = correct / len(y_test)

print("\nManual Accuracy:", round(manual_accuracy * 100, 2), "%")

# =============================================================
# 6. Misclassified Students
# =============================================================
misclassified = X_test[y_test != y_pred]

print("\nMisclassified Students:")
print(misclassified)

print("Total Misclassified:", len(misclassified))

# =============================================================
# 7. Train model with different random_state
# =============================================================
for rs in [0, 10, 42]:
    temp_model = DecisionTreeClassifier(random_state=rs)
    temp_model.fit(X_train, y_train)
    acc = accuracy_score(y_test, temp_model.predict(X_test))
    print(f"\nAccuracy with random_state={rs}:",
          round(acc * 100, 2), "%")

# =============================================================
# 8. Decision Tree Visualization
# =============================================================
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=X.columns, class_names=["Fail", "Pass"], filled=True)
plt.title("Decision Tree Visualization")
plt.show()

# =============================================================
# 9. Create New Feature: PerformanceIndex
# =============================================================
df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X_new = df.drop("FinalResult", axis=1)
y_new = df["FinalResult"]

Xn_train, Xn_test, yn_train, yn_test = train_test_split(
    X_new, y_new, test_size=0.3, random_state=42
)

model_new = DecisionTreeClassifier(random_state=42)
model_new.fit(Xn_train, yn_train)

acc_new = accuracy_score(yn_test, model_new.predict(Xn_test))
print("\nAccuracy with PerformanceIndex:", round(acc_new * 100, 2), "%")

# =============================================================
# 10. Train with max_depth=None
# =============================================================
deep_model = DecisionTreeClassifier(max_depth=None, random_state=42)
deep_model.fit(X_train, y_train)

train_acc = accuracy_score(y_train, deep_model.predict(X_train))
test_acc = accuracy_score(y_test, deep_model.predict(X_test))

print("\nTraining Accuracy:", round(train_acc * 100, 2), "%")
print("Testing Accuracy:", round(test_acc * 100, 2), "%")

if train_acc == 1.0 and test_acc < train_acc:
    print("Model is Overfitting because tree memorized training data.")