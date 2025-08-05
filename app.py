from flask import Flask, request, render_template
from parser import extract_text_from_pdf, parse_resume
from db import connect
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        file = request.files['resume']
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        text = extract_text_from_pdf(file_path)
        data = parse_resume(text)

        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO resumes (name, skills, education) VALUES (%s, %s, %s)",
                    (data['name'], data['skills'], data['education']))
        conn.commit()
        cur.close()
        conn.close()

        return f"Resume parsed and saved: {data}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
