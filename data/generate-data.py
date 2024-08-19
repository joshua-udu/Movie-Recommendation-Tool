import pandas as pd
import numpy as np

# Parameters
num_users = 1000
num_movies = 500
num_interactions = 1000  # Set to 1000 interactions

# Generate User IDs and Movie IDs
user_ids = [f"user_{i}" for i in range(1, num_users + 1)]
movie_ids = [f"movie_{i}" for i in range(1, num_movies + 1)]

# Generate Movie Metadata
np.random.seed(42)  # For reproducibility
movie_titles = [f"Movie Title {i}" for i in range(1, num_movies + 1)]
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance']
data_movies = {
    "movie_id": movie_ids,
    "title": movie_titles,
    "release_year": np.random.randint(1900, 2024, num_movies),
    "runtime_minutes": np.random.randint(60, 180, num_movies),
    "genre": np.random.choice(genres, num_movies),
    "rating": np.random.uniform(1.0, 10.0, num_movies)
}
movies_metadata = pd.DataFrame(data_movies)

# Simulate Viewing History
data_viewing = {
    "user_id": np.random.choice(user_ids, num_interactions),
    "movie_id": np.random.choice(movie_ids, num_interactions),
    "rating": np.random.randint(1, 6, num_interactions),
    "timestamp": pd.to_datetime(np.random.choice(pd.date_range('2023-01-01', '2024-01-01'), num_interactions)),
    "device": np.random.choice(['mobile', 'desktop', 'smart_tv'], num_interactions)
}
viewing_history = pd.DataFrame(data_viewing)

# Display Sample Data
print("Viewing History Sample:")
print(viewing_history.head())

print("\nMovies Metadata Sample:")
print(movies_metadata.head())

# Save to CSV for further use
viewing_history.to_csv('data/simulated_viewing_history.csv', index=False)
movies_metadata.to_csv('data/simulated_movies_metadata.csv', index=False)
