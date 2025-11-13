import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Size_sqft': [600, 750, 900, 1100, 850],
    'BHK': [1, 2, 2, 3, 2],
    'City': ['Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi'],
    'Rent': [25000, 22000, 18000, 32000, 21000]
}

df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=['City'], drop_first=True)
print(df_encoded)

X = df_encoded.drop('Rent', axis=1)
y = df_encoded['Rent']

model = LinearRegression()
model.fit(X, y)

print("\nModel Coefficients:")
for col, coef in zip(X.columns, model.coef_):
    print(f"{col}: {coef:.2f}")

new_house = pd.DataFrame({
    'Size_sqft': [1000],
    'BHK': [2],
    'City_Delhi': [0],
    'City_Mumbai': [1]
})
predicted_rent = model.predict(new_house)
print("\nPredicted Rent for Mumbai (1000 sqft, 2 BHK):", int(predicted_rent[0]))