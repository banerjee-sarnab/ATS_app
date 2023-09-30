from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

secret_key = os.urandom(24)
app.secret_key = secret_key

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the UPLOAD_FOLDER directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_score', methods=['POST'])
def calculate_score():
    if 'cv_file' not in request.files or 'jd_file' not in request.files:
        flash('Both CV and Job Description files are required.', 'error')
        return redirect(request.url)

    cv_file = request.files['cv_file']
    jd_file = request.files['jd_file']

    if cv_file.filename == '' or jd_file.filename == '':
        flash('Please select files for both CV and Job Description.', 'error')
        return redirect(request.url)

    if cv_file and allowed_file(cv_file.filename) and jd_file and allowed_file(jd_file.filename):
        cv_filename = secure_filename(cv_file.filename)
        jd_filename = secure_filename(jd_file.filename)

        cv_file.save(f'{app.config["UPLOAD_FOLDER"]}/{cv_filename}')
        jd_file.save(f'{app.config["UPLOAD_FOLDER"]}/{jd_filename}')

        cv_path = f'{app.config["UPLOAD_FOLDER"]}/{cv_filename}'
        jd_path = f'{app.config["UPLOAD_FOLDER"]}/{jd_filename}'

        # Process the CV and JD and calculate similarity
        similarity_score = calculate_similarity(cv_path, jd_path)

        return render_template('index.html', score=similarity_score)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'txt', 'doc', 'docx'}

def calculate_similarity(cv_path, jd_path):
    with open(jd_path, 'r') as f:
        jd = f.read()

    read = PdfReader(cv_path)
    n = len(read.pages)
    data = ""
    for i in range(n):
        page = read.pages[i]
        data += page.extract_text()

    data = " ".join(data.split('\n'))
    data = data.replace("\xa0", "")
    data = data.replace("\uf0b7", "")
    data = data.replace("\uf0a7", "")

    nlp = spacy.load("en_core_web_md")

    v1 = nlp(data).vector
    v2 = nlp(jd).vector

    similarity = cosine_similarity([v1], [v2])

    return round(similarity[0][0] * 100, 2)

if __name__ == '__main__':
    app.run(debug=True)
