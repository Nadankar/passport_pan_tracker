import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle  # For saving the model

# Load dataset
df = pd.read_csv("dataset.csv")

# Convert categorical variables to numeric
df["Type"] = df["Type"].map({"Passport": 1, "PAN": 0})
df["Verification_Status"] = df["Verification_Status"].map({"Completed": 1, "Incomplete": 0})
df["Criminal_Record"] = df["Criminal_Record"].map({"No": 0, "Yes": 1})

# Define Features (X) and Target Variable (Y)
X = df.drop(columns=["Approval_Time", "State"])  # Dropping State for now
y = df["Approval_Time"]

# Split dataset into Training & Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
