# %pip install --upgrade pandas numpy seaborn matplotlib scikit-learn

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# Read CSV
df = pd.read_csv("data/advertising.csv")

section("LAST 5 ROWS")
print(df.tail())

section("SHAPE")
print("Shape:", df.shape)

section("COLUMNS")
print("Columns:", df.columns.tolist())

section("DATA TYPES & INFO")
print(df.info())

section("MISSING VALUES")
print(df.isnull().sum())

section("STATISTICAL SUMMARY")
print(df.describe())

section("DUPLICATE ROWS")
print("Duplicate rows:", df.duplicated().sum())

# Generate Pair Plot
plt.figure(figsize=(12, 10))
pair_plot = sns.pairplot(df, diag_kind="hist", plot_kws={"alpha": 0.6})
pair_plot.fig.suptitle("Pair Plot of Advertising Data", y=1.00)
plt.tight_layout()
plt.show()

# TV sales can include linear regression model to predict sales based on TV advertising budget.
X = df[
    ["TV"]
]  # Accessing the feature variable 'TV' from the DataFrame as a 2D array for sklearn
y = df[
    "Sales"
]  # Accessing the target variable 'Sales' from the DataFrame as a 1D array for sklearn

# Generate Box Plot for TV
plt.figure(figsize=(10, 6))
sns.boxplot(y=df["TV"], palette="Set2")
plt.title("Box Plot of TV Advertising Budget", fontsize=14, fontweight="bold")
plt.ylabel("TV Budget", fontsize=12)
plt.tight_layout()
plt.show()

section("TV STATISTICS")
print(f"Min: {df['TV'].min()}")
print(f"Max: {df['TV'].max()}")
print(f"Mean: {df['TV'].mean():.2f}")
print(f"Median: {df['TV'].median()}")
print(f"Std Dev: {df['TV'].std():.2f}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

section("TRAIN/TEST SPLIT")
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_model.weights = lr_model.coef_[0]

section("MODEL PARAMETERS")
print(f"Coefficient (Weight): {lr_model.weights:.4f}")  # Slope of the regression line
print(f"Intercept: {lr_model.intercept_:.4f}")  # Intercept of the regression line

# Overfitting check: Train and Test Scores
train_score = lr_model.score(X_train, y_train)
test_score = lr_model.score(X_test, y_test)

section("OVERFITTING CHECK (R^2 SCORES)")
print(f"Training Score (R^2): {train_score:.4f}")
print(f"Testing Score (R^2): {test_score:.4f}")

# Train RMSE
train_predictions = lr_model.predict(X_train)
train_rmse = np.sqrt(metrics.mean_squared_error(y_train, train_predictions))

# Test RMSE
test_predictions = lr_model.predict(X_test)
test_rmse = np.sqrt(metrics.mean_squared_error(y_test, test_predictions))

section("RMSE (ROOT MEAN SQUARED ERROR)")
print(f"Train RMSE: {train_rmse:.4f}")
print(f"Test RMSE: {test_rmse:.4f}")


section("MAE")
print(f"Train MAE: {metrics.mean_absolute_error(y_train, train_predictions):.4f}")
print(f"Test MAE: {metrics.mean_absolute_error(y_test, test_predictions):.4f}")

section("R2 Score")
print(f"Train R2 Score: {lr_model.score(X_train, y_train):.4f}")
print(f"Test R2 Score: {lr_model.score(X_test, y_test):.4f}")


# Prediction x = 200
section("PREDICT")
tv_budget = 200
prediction = lr_model.predict(
    pd.DataFrame({"TV": [tv_budget]})
)
print(f"TV Advertising Budget: {tv_budget}")
print(f"Predicted Sales: {prediction[0]:.4f}")