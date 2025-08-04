from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the saved scaler and DBSCAN model
scaler = joblib.load('scaler.joblib')
dbscan_model = joblib.load('dbscan_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input features from form
        features = [
            float(request.form['social_energy']),
            float(request.form['alone_time_preference']),
            float(request.form['talkativeness']),
            float(request.form['deep_reflection']),
            float(request.form['group_comfort']),
            float(request.form['party_liking']),
            float(request.form['listening_skill']),
            float(request.form['empathy']),
            float(request.form['creativity']),
            float(request.form['organization']),
            float(request.form['leadership']),
            float(request.form['risk_taking']),
            float(request.form['public_speaking_comfort']),
            float(request.form['curiosity']),
            float(request.form['routine_preference']),
            float(request.form['excitement_seeking']),
            float(request.form['friendliness']),
            float(request.form['emotional_stability']),
            float(request.form['planning']),
            float(request.form['spontaneity']),
            float(request.form['adventurousness']),
            float(request.form['reading_habit']),
            float(request.form['sports_interest']),
            float(request.form['online_social_usage']),
            float(request.form['travel_desire']),
            float(request.form['gadget_usage']),
            float(request.form['work_style_collaborative']),
            float(request.form['decision_speed']),
            float(request.form['stress_handling'])
        ]

        # Convert to numpy array and scale
        final_features = np.array(features).reshape(1, -1)
        scaled_features = scaler.transform(final_features)

        # Predict cluster
        cluster = dbscan_model.fit_predict(scaled_features)[0]  # Predict for new data

        return render_template('index.html', prediction_text=f'Predicted Cluster: {cluster}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
