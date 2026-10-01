import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Sample communication link data
data = {
    "Distance": [100, 200, 300, 150, 400, 250, 120, 350, 180, 450,
                 220, 320, 140, 380, 260, 110, 420, 230, 170, 360],

    "Signal_Strength": [-50, -55, -65, -52, -75, -60, -48, -70, -54, -80,
                        -58, -68, -51, -72, -62, -47, -78, -59, -53, -71],

    "Latency": [20, 25, 35, 22, 60, 30, 18, 55, 24, 70,
                28, 40, 21, 58, 32, 17, 65, 29, 23, 50],

    "Packet_Loss": [1, 2, 4, 1, 8, 3, 1, 7, 2, 10,
                    2, 5, 1, 8, 3, 1, 9, 2, 2, 6],

    "Connection_Duration": [90, 85, 70, 95, 50, 75, 98, 55, 88, 40,
                            82, 65, 92, 48, 78, 99, 45, 84, 91, 60],

    "Quality": [
        "Good", "Good", "Moderate", "Good", "Poor",
        "Moderate", "Good", "Poor", "Good", "Poor",
        "Good", "Moderate", "Good", "Poor", "Moderate",
        "Good", "Poor", "Good", "Good", "Moderate"
    ]
}

df = pd.DataFrame(data)

# Separate input and output
X = df.drop("Quality", axis=1)
y = df["Quality"]

# Convert labels into numbers
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "SVM": SVC()
}

print("========================================")
print("   SATELLITE LINK QUALITY PREDICTION")
print("========================================")

# Train and compare models
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{name}: {accuracy * 100:.2f}%")