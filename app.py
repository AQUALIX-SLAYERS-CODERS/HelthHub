from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.tree import DecisionTreeClassifier

app = Flask(http://localhost:5000)
app = Flask(http://localhost:5000)
CORS(app) 

# Sample trained model (replace this with your actual model)
model = DecisionTreeClassifier()

# Sample route for AI prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict([data['age'], data['exercise'], data['skincare'], data['health_condition'], data['sunscreen'], data['limitations']])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
