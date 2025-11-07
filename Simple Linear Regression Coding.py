import numpy as np
from sklearn.linear_model import LinearRegression

hours=np.array([[1.5],[2.0],[2.5],[3.0],[3.5],[4.0],[4.5],[5.0]])
score=np.array([40,45,50,55,60,65,70,75])

model = LinearRegression()
model.fit(hours,score)

new_hours=np.array([[3.8]])
new_score=model.predict(new_hours)
print(new_score)