import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('path_to_your_file/MLS.csv')

# Preprocessing
# Convert 'Date' to datetime and calculate months since the earliest date
data['Date'] = pd.to_datetime(data['Date'])
min_date = data['Date'].min()
data['MonthsSinceMin'] = ((data['Date'] - min_date) / np.timedelta64(1, 'M')).astype(int)

# Select features and target variable
features = ['CompIndex', 'SFDetachIndex', 'SFAttachIndex', 'THouseIndex', 'ApartIndex', 'MonthsSinceMin']
target = 'CompBenchmark'

# Drop rows with missing values in selected columns
data_clean = data.dropna(subset=[target] + features)

# Split data into features (X) and target (y)
X = data_clean[features]
y = data_clean[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print results
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Scatter plot of Actual vs Predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Home Prices')
plt.show()
