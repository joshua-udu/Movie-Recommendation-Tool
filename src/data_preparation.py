import pandas as pd
from surprise import Dataset, Reader

def load_data(viewing_history_path, movie_metadata_path):
    viewing_history = pd.read_csv(viewing_history_path)
    movie_metadata = pd.read_csv(movie_metadata_path)
    return viewing_history, movie_metadata

def prepare_data(viewing_history):
    reader = Reader(rating_scale=(1, 10))  # Adjust scale if needed
    data = Dataset.load_from_df(viewing_history[['user_id', 'movie_id', 'rating']], reader)
    return data
