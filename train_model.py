import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Load CSV created in Step 6
df = pd.read_csv("network_data.csv")

# Create a sample label
# Packets larger than 100 bytes -> Suspicious (1)
# Packets 100 bytes or less -> Normal (0)
threshold = df["Packet Length"].median()
df["Label"] = (df["Packet Length"] > threshold).astype(int)

print(df["Label"].value_counts())




# Encode protocol names (TCP, UDP, DNS, etc.)
encoder = LabelEncoder()
df["Protocol"] = encoder.fit_transform(df["Protocol"])

# Features
X = df[["Protocol", "Packet Length"]]

# Target
y = df["Label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Sample packet for prediction
sample_packet = [[1, 150]]

prediction = model.predict(sample_packet)

if prediction[0] == 1:
    print("Prediction: Suspicious Traffic")
else:
    print("Prediction: Normal Traffic")

# Generate Confusion Matrix
cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Plot Confusion Matrix
plt.imshow(cm, interpolation='nearest', cmap='Blues')
plt.title("Confusion Matrix")
plt.colorbar()

plt.xticks([0,1], ["Normal","Suspicious"])
plt.yticks([0,1], ["Normal","Suspicious"])

plt.xlabel("Predicted")
plt.ylabel("Actual")

for i in range(len(cm)):
    for j in range(len(cm[0])):
        plt.text(j, i, cm[i][j], ha="center", va="center")

plt.savefig("confusion_matrix.png")
plt.show()

# Feature Importance Graph
features = ["Protocol", "Packet Length"]
importance = model.feature_importances_

print("Feature Importance:", importance)

plt.figure(figsize=(6,4))
plt.bar(features, importance)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.show()
