import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#create the data
data ={
      'study_hours': [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
        'sleep_hours': [8.0, 7.0, 6.5, 7.0, 6.0, 8.0, 7.5, 6.5, 7.0, 6.0],
        'previous_score': [35, 40, 45, 50, 55, 60, 62, 65, 68, 70],
        'exam_score': [40, 45, 48, 55, 58, 65, 70, 72, 78, 80]
}

df=pd.DataFrame(data)

X = df[['study_hours', 'sleep_hours', 'previous_score']]
y = df['exam_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (R²):", r2)