from flask import Flask, render_template, request
import PyPDF2
import google.generativeai as genai

app = Flask(__name__)

# Add your Gemini API Key
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")

def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""

    if request.method == "POST":
        pdf = request.files["resume"]

        text = extract_text(pdf)

        prompt = f"""
        Analyze this resume and give:
        1. Skills
        2. Missing skills
        3. Improvement suggestions

        Resume:
        {text}
        """

        result = model.generate_content(prompt)
        response = result.text

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
