import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def customer_churn_model():
    # Dataset (X = features, y = output)
    X = np.array([
        [25, 500, 12, 1, 2],
        [30, 700, 24, 0, 1],
        [45, 1200, 6, 5, 8],
        [50, 900, 15, 2, 4],
        [28, 650, 18, 1, 1],
        [35, 800, 10, 0, 2],
        [48, 1400, 4, 7, 9],
        [52, 1600, 3, 8, 10],
        [27, 550, 20, 0, 1],
        [42, 1300, 8, 4, 7]
    ])

    y = np.array([0,0,1,0,0,0,1,1,0,1])

    # Step 1: Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Step 2: Train model
    model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=500, random_state=42)
    model.fit(X_scaled, y)

    # Step 3: Accuracy
    y_pred = model.predict(X_scaled)
    print("Customer Churn Accuracy:", accuracy_score(y, y_pred))

    # Step 4: Test input
    new_customer = np.array([[46, 1450, 5, 6, 9]])
    new_scaled = scaler.transform(new_customer)

    prediction = model.predict(new_scaled)

    print("Prediction:", "Customer will leave" if prediction[0] == 1 else "Customer will stay")

customer_churn_model()