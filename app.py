from flask import Flask, render_template, request
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    content = request.form['content']
    summary = generate_summary(content)
    return summary

def generate_summary(content):
    sentences = sent_tokenize(content)
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(sentences)
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    summary = ' '.join(sentences[i] for i in sorted(range(len(similarity_matrix[0])), key=lambda x: similarity_matrix[0][x], reverse=True)[:3])
    return summary

if __name__ == '__main__':
    app.run(debug=True)
