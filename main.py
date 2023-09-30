from PyPDF2 import PdfReader
import spacy


read = PdfReader('sample cv.pdf')

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

with open("jd.txt") as f:
    jd = f.readlines()

jd = " ".join(jd)

v2 = nlp(jd).vector

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity([v1], [v2])

print("Score : ", similarity[0][0] * 100, "%")

