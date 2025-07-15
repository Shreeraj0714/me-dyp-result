from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def load_results():
    with open('results.json') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/result', methods=['POST'])
def result():
    mobile = request.form['mobile']
    results_data = load_results()  # <-- load fresh every time
    if mobile in results_data:
        student = results_data[mobile]
        return render_template('result.html', student=student, mobile=mobile)
    else:
        error = "Result not available for this mobile number."
        return render_template('login.html', error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


