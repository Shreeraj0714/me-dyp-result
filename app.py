from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Load results data
with open('results.json') as f:
    results_data = json.load(f)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/result', methods=['POST'])
def result():
    mobile = request.form['mobile']
    if mobile in results_data:
        student = results_data[mobile]
        return render_template('result.html', student=student, mobile=mobile)
    else:
        error = "Result not available for this mobile number."
        return render_template('login.html', error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

