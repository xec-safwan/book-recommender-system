from flask import Flask, render_template
import pickle
import pandas as pd






app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    filename = 'popular.pkl'
    popular_df = pickle.load(open(filename, 'rb'))
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_rating'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    pt = pickle.load(open('pt.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
    return render_template('recommend.html')


if __name__ == '__main__':
    app.run(debug=True)
