# ==========================================
# Student Performance Clustering (K-Means)
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def MarvellousStudentCluster():

    # =========================
    # 1. Load Dataset
    # =========================
    df = pd.read_csv("student.csv")   # dataset file

    print("First 5 Rows:\n", df.head())
    print("\nInfo:\n")
    print(df.info())

    # =========================
    # 2. Select Required Features
    # =========================
    features = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
    data = df[features]

    # =========================
    # 3. Handle Missing Values
    # =========================
    data.fillna(data.mean(), inplace=True)

    # =========================
    # 4. Feature Scaling
    # =========================
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # =========================
    # 5. Find Optimal Clusters (Elbow Method)
    # =========================
    wcss = []

    for i in range(1, 6):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(scaled_data)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 6), wcss)
    plt.title("Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.show()

    # =========================
    # 6. Apply K-Means (3 Clusters)
    # =========================
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(scaled_data)

    # =========================
    # 7. Analyze Clusters
    # =========================
    print("\nCluster Summary:\n")
    print(df.groupby('Cluster')[features].mean())

    # =========================
    # 8. Label Clusters
    # =========================
    # Based on mean values
    cluster_labels = {
        0: "Top Performers",
        1: "Average Students",
        2: "Struggling Students"
    }

    df['Category'] = df['Cluster'].map(cluster_labels)

    print("\nSample Output:\n")
    print(df[['G1','G2','G3','studytime','failures','absences','Category']].head())

    # =========================
    # 9. Visualization
    # =========================
    plt.scatter(df['G3'], df['studytime'], c=df['Cluster'])
    plt.title("Student Clusters")
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Study Time")
    plt.show()

    # =========================
    # 10. Save Output
    # =========================
    df.to_csv("student_clusters.csv", index=False)
    print("\nClusters saved to student_clusters.csv")


# =========================
# Main Function
# =========================
def main():
    print("----- Student Clustering System -----")
    MarvellousStudentCluster()


if __name__ == "__main__":
    main()