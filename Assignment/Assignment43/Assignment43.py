import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def MarvellousPlayPredictor():

    # Step 1 : Load Dataset
    df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    print("Dataset:")
    print(df)

    # Step 2 : Data Preparation (Encoding)
    le_weather = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df['Weather'] = le_weather.fit_transform(df['Weather'])
    df['Temperature'] = le_temp.fit_transform(df['Temperature'])
    df['Play'] = le_play.fit_transform(df['Play'])

    # Step 3 : Train Model
    X = df[['Weather','Temperature']]
    y = df['Play']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=1)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train, y_train)

    # Step 4 : Testing
    predictions = model.predict(X_test)

    print("\nPredicted Values :", predictions)
    print("Actual Values :", y_test.values)

    # Step 5 : Accuracy
    accuracy = accuracy_score(y_test, predictions)

    print("\nAccuracy :", accuracy * 100, "%")

    # Predict New Input
    weather = input("\nEnter Weather (Sunny/Overcast/Rainy): ")
    temperature = input("Enter Temperature (Hot/Mild/Cool): ")

    weather = le_weather.transform([weather])
    temperature = le_temp.transform([temperature])

    result = model.predict([[weather[0], temperature[0]]])

    if result[0] == 1:
        print("Play = Yes")
    else:
        print("Play = No")


def main():

    print("---- Marvellous Play Predictor ----")

    MarvellousPlayPredictor()


if __name__ == "__main__":
    main()