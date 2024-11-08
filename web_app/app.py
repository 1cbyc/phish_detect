from flask import Flask, render_template, request
from src.phish_detection_model import load_model, predict_url

app = Flask(__name__)
model = load_model()
preprocessor = None  # Load your preprocessor if saved separately

@app.route("/", methods=["GET", "POST"])
def index():
    prediction, confidence = None, None
    if request.method == "POST":
        url = request.form["url"]
        prediction, confidence = predict_url(url, model, preprocessor)
        confidence = round(confidence[0][1] * 100, 2)  # Assuming 2nd column is phishing probability
    
    return render_template("index.html", prediction=prediction, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
