# [A,B,C,D]
# X[1,2,3,6]
# Y[2,3,1,5]
# [R,R,B,B]

# Predict(2,2) -> ?

import math

# Dataset
students = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]

# Input
study = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

k = 3
distances = []

# Calculate distance
for data in students:
    s, a, label = data
    distance = math.sqrt((study - s)**2 + (attendance - a)**2)
    distances.append((distance, label))

# Sort
distances.sort()

# Majority voting
votes = {}
for i in range(k):
    label = distances[i][1]
    votes[label] = votes.get(label, 0) + 1

prediction = max(votes, key=votes.get)

print("\nPredicted Result:", prediction)
