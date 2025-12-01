import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SAVED = os.path.join(BASE_DIR, "models")

app = Flask(__name__)
CORS(app)

def load_model(filename):
    path = os.path.join(SAVED, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    return None

# Load existing models
diabetes_model = load_model("diabetes_model.sav")
heart_model = load_model("heart_disease_model.sav")
parkinsons_model = load_model("parkinsons_model.sav")

def train_autism_model():
    # Train an improved RandomForest on A1..A10 and age with better hyperparameters
    try:
        df = pd.read_csv(os.path.join(BASE_DIR, "data", "autism.csv"))
    except Exception:
        return None

    cols = [f"A{i}_Score" for i in range(1, 11)] + ["age"]
    for c in cols:
        if c not in df.columns:
            # fallback: try lowercase with spaces
            pass

    # Keep numeric columns available
    df_sub = df[[c for c in cols if c in df.columns]].copy()
    df_sub = df_sub.dropna()
    if df_sub.shape[0] < 10:
        return None

    # Convert non-numeric age if needed
    df_sub["age"] = pd.to_numeric(df_sub["age"], errors="coerce").fillna(df_sub["age"].mean())

    X = df_sub[[c for c in cols if c in df_sub.columns]]
    # target column name
    target_col = None
    for candidate in ["Class/ASD", "ASD", "result", "Class"]:
        if candidate in df.columns:
            target_col = candidate
            break
    if target_col is None:
        return None

    y = df.loc[df_sub.index, target_col]

    # Train an improved RandomForest with better hyperparameters
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        class_weight='balanced'
    )
    clf.fit(X, y)

    # Save model
    out_path = os.path.join(SAVED, "autism_model.sav")
    with open(out_path, "wb") as f:
        pickle.dump(clf, f)
    return clf

# Ensure autism model exists
autism_model = load_model("autism_model.sav")
if autism_model is None:
    try:
        autism_model = train_autism_model()
    except Exception:
        autism_model = None

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "running",
        "models": {
            "diabetes": diabetes_model is not None,
            "heart": heart_model is not None,
            "parkinsons": parkinsons_model is not None,
            "autism": autism_model is not None
        }
    })

@app.route("/predict/<model_name>", methods=["POST"])
def predict(model_name):
    data = request.get_json() or {}
    features = data.get("features")

    model = None
    if model_name == "diabetes":
        model = diabetes_model
    elif model_name == "heart":
        model = heart_model
    elif model_name == "parkinsons":
        model = parkinsons_model
    elif model_name == "autism":
        model = autism_model

    if model is None:
        return jsonify({"error": "Model not available on server."}), 500

    # For autism we accept answers from 20-question assessment
    if model_name == "autism":
        # if features provided directly (11 features: A1-A10 + age)
        if features and len(features) >= 11:
            arr = np.array(features).reshape(1, -1)
        else:
            # Convert 20 answers to 10 A-scores by averaging pairs + risk percentage
            answers = data.get("answers", {})
            rp = float(data.get("riskPercentage", 0))
            
            if answers:
                # Map 20 questions to 10 A-scores (averaging pairs for better granularity)
                # Questions 1-2 -> A1, 3-4 -> A2, etc.
                a_scores = []
                answer_list = [answers.get(str(i), 2) for i in range(20)]  # default to 2 (sometimes)
                
                # Average every 2 questions to get 10 A-scores
                for i in range(0, 20, 2):
                    avg_score = (answer_list[i] + answer_list[i+1]) / 2
                    # Convert to binary: > 2 means 1 (concern), <= 2 means 0 (typical)
                    a_scores.append(1 if avg_score > 2 else 0)
                
                # Add age estimate (use 30 as default or calculate from risk)
                age = float(data.get("age", 30.0))
                a_scores.append(age)
                arr = np.array([a_scores])
            else:
                # Fallback using risk percentage only
                # Create 11 features based on risk percentage
                dummy_features = [1 if rp > 50 else 0] * 10 + [30.0]
                arr = np.array([dummy_features])
        
        pred = model.predict(arr)
        prob = model.predict_proba(arr)[0] if hasattr(model, 'predict_proba') else None
        
        result = {
            "prediction": int(pred[0]),
            "result": "High Risk" if int(pred[0]) == 1 else "Low Risk"
        }
        
        if prob is not None:
            result["confidence"] = float(max(prob))
            result["risk_score"] = float(prob[1]) * 100  # Probability of positive class
        
        return jsonify(result)

    if not features:
        return jsonify({"error": "Features missing"}), 400

    try:
        arr = np.array(features).reshape(1, -1)
        pred = model.predict(arr)
        # If model outputs probabilities, present label
        result_text = "Positive" if int(pred[0]) == 1 else "Negative"
        return jsonify({
            "prediction": int(pred[0]),
            "result": result_text
        })
    except Exception as e:
        return jsonify({"error": f"Prediction error: {str(e)}. Please check your input features."}), 500

if __name__ == "__main__":
    print("Starting Flask server...")
    print(f"Diabetes model loaded: {diabetes_model is not None}")
    print(f"Heart model loaded: {heart_model is not None}")
    print(f"Parkinsons model loaded: {parkinsons_model is not None}")
    print(f"Autism model loaded: {autism_model is not None}")
    app.run(host="0.0.0.0", port=5000, debug=False)
