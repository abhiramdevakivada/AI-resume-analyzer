from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']

    if file.filename == '':
        return render_template(
            'index.html',
            response="Please select a resume."
        )

    filename = file.filename
    upload_path = os.path.join("uploads", filename)

    os.makedirs("uploads", exist_ok=True)
    file.save(upload_path)

    # AI analysis logic here
    result = f"Resume uploaded successfully: {filename}"

    return render_template(
        'index.html',
        response=result
    )

if __name__ == '__main__':
    app.run(debug=True)
