import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load data
df = pd.read_csv("Artificial_Neural_Network_Case_Study_data.csv")

print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())

# Drop unnecessary columns
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# Encode categorical variables
le_geography = LabelEncoder()
le_gender = LabelEncoder()

df['Geography'] = le_geography.fit_transform(df['Geography'])
df['Gender'] = le_gender.fit_transform(df['Gender'])

print("\nData after encoding:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# Split features & target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

print(f"\nFeatures shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape}")
print(f"Test set size: {X_test.shape}")

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save scaler
pickle.dump(scaler, open("scaler.pkl", "wb"))
print("\nScaler saved!")

# Build ANN
print("\nBuilding ANN model...")
model = Sequential()
model.add(Dense(10, activation='relu', input_dim=X_train_scaled.shape[1]))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train
print("Training model...")
history = model.fit(X_train_scaled, y_train, epochs=10, batch_size=10, verbose=1)

# Evaluate
print("\nEvaluating model...")
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

# Save model
model.save("model.h5")
print("\n✓ Model saved successfully!")
print("✓ Scaler saved successfully!")
print("\nAll artifacts ready for API deployment!")
