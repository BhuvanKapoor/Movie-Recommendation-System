import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendation(title):
    movies_data = pd.read_csv("movies.csv")
    selected_features = ['genres','keywords','tagline','cast','director']
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna("")

    combined_features = movies_data['genres'] + movies_data['keywords'] + movies_data['tagline'] + movies_data['cast'] + movies_data['director']

    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)
    similarity = cosine_similarity(feature_vectors)
    list_of_all_titles = movies_data['title'].tolist()
    movie_name = title
    find_close_match=difflib.get_close_matches(movie_name,list_of_all_titles)
    close_match=find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies=sorted(similarity_score, key=lambda x:x[1],reverse=True)
    sorted_similar_movies_top = sorted_similar_movies[:10]
    movie_index = [i[0] for i in sorted_similar_movies_top]
    
    return movies_data['title'].iloc[movie_index]



# i = 1
# for movie in sorted_similar_movies:
#     index = movie[0]
#     title_from_index = movies_data[movies_data.index==index]['title'].values[0]
#     if (i<11):
#         print(i, '.',title_from_index)
#         i+=1