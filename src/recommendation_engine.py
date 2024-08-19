import pandas as pd
from .model_filtering import train_user_based_model, get_item_similarities
from .data_preparation import prepare_data
from .sentiment_analysis import analyze_sentiment


def get_user_recommendations(model, user_id, movie_ids, movie_metadata):
    recommendations = []
    for movie_id in movie_ids:
        pred = model.predict(user_id, movie_id)
        recommendations.append({
            'movie_id': movie_id,
            'rating': pred.est,
            'title': movie_metadata.loc[movie_metadata['movie_id'] == movie_id, 'title'].values[0],
            'genre': movie_metadata.loc[movie_metadata['movie_id'] == movie_id, 'genre'].values[0]
        })
    recommendations.sort(key=lambda x: x['rating'], reverse=True)
    return recommendations[:10] 

def get_recommendations(user_id, user_input, viewing_history, movie_metadata):
    # Prepare data
    data = prepare_data(viewing_history)
    
    # Train models
    user_based_model = train_user_based_model(data)
    similarity_matrix = get_item_similarities(viewing_history)
    
    # User-based recommendations
    movie_ids = viewing_history['movie_id'].unique()
    user_recommendations = get_user_recommendations(user_based_model, user_id, movie_ids, movie_metadata)
    
    # Emotion-based recommendations
    mood = analyze_sentiment(user_input)
    emotion_based_recommendations = get_emotion_based_recommendations(mood, movie_metadata)
    
    # Combine results
    all_recommendations = pd.DataFrame(user_recommendations).drop_duplicates()
    
    return all_recommendations, mood


def get_similar_movies(movie_id, similarity_matrix, top_n=10):
    similar_movies = similarity_matrix[movie_id].sort_values(ascending=False)
    return similar_movies.head(top_n).index.tolist()

def get_emotion_based_recommendations(mood, movie_metadata):
    if mood == 'positive':
        # Recommend uplifting genres
        recommended_movies = movie_metadata[movie_metadata['genre'].str.contains('Comedy|Action|Sci-Fi')]
    elif mood == 'negative':
        # Recommend comforting genres
        recommended_movies = movie_metadata[movie_metadata['genre'].str.contains('Drama|Romance|Horror')]
    else:
        # Default to a mix if mood is neutral or undefined
        recommended_movies = movie_metadata.head(10)
    
    return recommended_movies.head(10)

