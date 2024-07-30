import joblib
import numpy as np
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('smart-agriculture.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the POST request
        data = request.json
        features = [data['N'], data['K'], data['P'], data['temperature'], 
                    data['humidity'], data['ph'], data['rainfall']]
        
        # Convert features to numpy array and reshape for prediction
        features = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)[0]
        return jsonify({'crop': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
