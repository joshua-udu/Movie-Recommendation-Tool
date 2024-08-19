from surprise import SVD
from surprise.model_selection import train_test_split
import pandas as pd


def train_user_based_model(data):
    trainset, testset = train_test_split(data, test_size=0.2)
    model = SVD()
    model.fit(trainset)
    return model

def get_item_similarities(viewing_history):
    # Remove duplicates based on user_id and movie_id
    viewing_history = viewing_history.drop_duplicates(subset=['user_id', 'movie_id'])
    
    # Pivot the data
    pivot_table = viewing_history.pivot(index='user_id', columns='movie_id', values='rating')
    
    # Compute similarity matrix (for example, using cosine similarity)
    from sklearn.metrics.pairwise import cosine_similarity
    similarity_matrix = pd.DataFrame(
        cosine_similarity(pivot_table.fillna(0).T),
        index=pivot_table.columns,
        columns=pivot_table.columns
    )
    return similarity_matrix
