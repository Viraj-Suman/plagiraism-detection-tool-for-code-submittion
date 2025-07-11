from flask import Flask, render_template, request
from difflib import SequenceMatcher
import re

app = Flask(__name__)

def normalize_code(code):
    # Remove comments and excess whitespace
    code = re.sub(r'//.*?$|/\*.*?\*/', '', code, flags=re.DOTALL | re.MULTILINE)
    code = re.sub(r'\s+', ' ', code)
    return code.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    similarity = 0
    if request.method == 'POST':
        code1 = request.form['code1']
        code2 = request.form['code2']

        norm1 = normalize_code(code1)
        norm2 = normalize_code(code2)

        matcher = SequenceMatcher(None, norm1, norm2)
        similarity = round(matcher.ratio() * 100, 2)

        if similarity >= 70:
            result = f"⚠️ Similar Code Detected - {similarity}% match"
        else:
            result = f"✅ No Major Similarity - {similarity}% match"

    return render_template('index.html', result=result, similarity=similarity)

if __name__ == '__main__':
    app.run(debug=True)
