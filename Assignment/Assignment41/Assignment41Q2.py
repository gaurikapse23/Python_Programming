# [A,B,C,D]
# X[1,2,3,6]
# Y[2,3,1,5]
# [R,R,B,B]

# Predict(2,2) -> ?


import math

dataset = {
    "A": (1, 2, "Red"),
    "B": (2, 3, "Red"),
    "C": (3, 1, "Blue"),
    "D": (6, 5, "Blue")
}

x = 2
y = 2

def knn_predict(k):
    distances = []

    for point, values in dataset.items():
        x1, y1, label = values
        distance = math.sqrt((x - x1)**2 + (y - y1)**2)
        distances.append((distance, label))

    distances.sort()

    k = min(k,len(distances))
    
    votes = {}
    for i in range(k):
        label = distances[i][1]
        votes[label] = votes.get(label, 0) + 1

    return max(votes, key=votes.get)

print("Prediction Results:")
for k in [1, 3, 5]:
    print("K =", k, "->", knn_predict(k))