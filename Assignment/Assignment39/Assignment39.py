# -------------------------------------------------------------
# Student Performance ML - Decision Tree Implementation
# -------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# -------------------------------------------------------------
# 1. Load Dataset
# -------------------------------------------------------------
df = pd.read_csv("student_performance_ml.csv")

print("First 5 Records:")
print(df.head())

print("\nDataset Shape:", df.shape)

# -------------------------------------------------------------
# 2. Define Features and Target
# -------------------------------------------------------------
X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

# -------------------------------------------------------------
# 3. Train-Test Split
# -------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# -------------------------------------------------------------
# 4. Train Decision Tree Model
# -------------------------------------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# -------------------------------------------------------------
# 5. Prediction
# -------------------------------------------------------------
y_pred = model.predict(X_test)

print("\nActual vs Predicted (First 10):")
for actual, pred in zip(y_test[:10], y_pred[:10]):
    print("Actual:", actual, "Predicted:", pred)

# -------------------------------------------------------------
# 6. Accuracy Calculation
# -------------------------------------------------------------
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# -------------------------------------------------------------
# 7. Confusion Matrix
# -------------------------------------------------------------
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix")
plt.show()

print("\nConfusion Matrix:")
print(cm)

# -------------------------------------------------------------
# Confusion Matrix Explanation
# -------------------------------------------------------------
print("\nExplanation:")
print("True Positive  (TP): Correctly predicted Pass")
print("True Negative  (TN): Correctly predicted Fail")
print("False Positive (FP): Predicted Pass but actually Fail")
print("False Negative (FN): Predicted Fail but actually Pass")

# -------------------------------------------------------------
# 8. Training vs Testing Accuracy
# -------------------------------------------------------------
train_accuracy = accuracy_score(y_train, model.predict(X_train))
test_accuracy = accuracy_score(y_test, y_pred)

print("\nTraining Accuracy:", round(train_accuracy * 100, 2), "%")
print("Testing Accuracy :", round(test_accuracy * 100, 2), "%")

if train_accuracy > test_accuracy:
    print("Model may be Overfitting.")
elif train_accuracy < test_accuracy:
    print("Model may be Underfitting.")
else:
    print("Model is Balanced.")

# -------------------------------------------------------------
# 9. Train 3 Models with Different max_depth
# -------------------------------------------------------------
depths = [1, 3, None]

for depth in depths:
    temp_model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    temp_model.fit(X_train, y_train)
    temp_pred = temp_model.predict(X_test)
    temp_acc = accuracy_score(y_test, temp_pred)

    print(f"\nTesting Accuracy with max_depth={depth}:",
          round(temp_acc * 100, 2), "%")

# -------------------------------------------------------------
# 10. Predict New Student
# -------------------------------------------------------------
new_student = [[6, 85, 66, 7, 7]]
prediction = model.predict(new_student)

print("\nPrediction for New Student:")
if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")

# -------------------------------------------------------------
# Final Conclusion
# -------------------------------------------------------------
print("\nConclusion:")
print("StudyHours, Attendance, and PreviousScore strongly affect performance.")
print("Proper depth selection avoids overfitting.")
print("Decision Tree works well for this classification problem.")