from sklearn.tree import DecisionTreeClassifier

# Sample dataset (age, exercise level, skincare routine, pre-existing health condition, sunscreen usage, limitations)
# Format: [Age, Exercise Level, Skincare Routine, Pre-existing Health Condition, Sunscreen Usage, Limitations]
data = [
    [25, 2, 0, 0, 1, 0],  # Example data point
    # Add more data points based on the responses from the web form
]

# Labels indicating whether to consult a doctor (0 for No, 1 for Yes)
labels = [0, 1]  # Example labels

# Create a decision tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(data, labels)

# Now, you can use this model to make predictions

# Example: Predict whether a person with specific characteristics should consult a doctor
new_data_point = [[35, 3, 1, 1, 0, 0]]  # Example data point based on user responses
prediction = model.predict(new_data_point)

# Interpret the prediction
if prediction[0] == 1:
    print("You should consult a doctor.")
else:
    print("You may not need to consult a doctor.")

