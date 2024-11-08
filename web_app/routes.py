from flask import Flask, render_template, request, redirect, url_for
import joblib

app = Flask(__name__)
model = joblib.load('src/phish_detection_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    url = request.form.get('url')
    prediction = model.predict([url])[0]
    result = "Phishing" if prediction == 1 else "Legitimate"
    return render_template('result.html', url=url, result=result)

if __name__ == '__main__':
    app.run(debug=True)
