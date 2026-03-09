import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    'TV':[230.1,44.5,17.2,151.5,180.8,8.7,57.5,120.2,8.6,199.8],
    'Radio':[37.8,39.3,45.9,41.3,10.8,48.9,32.8,19.6,2.1,2.6],
    'Newspaper':[69.2,45.1,69.3,58.5,58.4,75.0,23.5,11.6,1.0,21.2],
    'Sales':[22.1,10.4,9.3,18.5,12.9,7.2,11.8,13.2,4.8,10.6]
}

df = pd.DataFrame(data)

X = df[['TV','Radio','Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5,random_state=0)

model = LinearRegression()

model.fit(X_train,y_train)

predictions = model.predict(X_test)

result = pd.DataFrame({
    'Actual Sales': y_test,
    'Predicted Sales': predictions
})

print(result)