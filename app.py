from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = pd.read_csv('train_data.csv')

tfv = TfidfVectorizer
vectors = tfv.fit_transform(data['tags'])
similarity = cosine_similarity(vectors)


def recommend_movie(movie):
    if movie not in data['title'].unique():
        return []
    else:
        i = data.loc[data['title'] == movie].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        lst = lst[1:11]
        result = []
        for i in range(len(lst)):
            a = lst[i][0]
            result.append(data['title'][a])
        return result


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html')


@app.route('/predict', methods=['POST'])
def predict():
    movie_name = request.form.get('Movie Name')
    pred = recommend_movie(movie=movie_name)
    return render_template('base.html', data=pred, len=len(pred))


if __name__ == "__main__":
    app.run()