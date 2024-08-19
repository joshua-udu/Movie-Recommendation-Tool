from flask import Flask, render_template, request
import pandas as pd
from src.data_preparation import load_data
from src.recommendation_engine import get_recommendations
app = Flask(__name__)

# Load data once at the start
viewing_history, movie_metadata = load_data('data/simulated_viewing_history.csv', 'data/simulated_movies_metadata.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = pd.DataFrame()
    mood = ""
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_input = request.form['user_input']

         # Validate user input
        if user_id and user_input:
            try:
                # Get recommendations based on user input
                recommendations, mood = get_recommendations(user_id, user_input, viewing_history, movie_metadata)
            except Exception as e:
                # Handle exceptions gracefully
                recommendations = pd.DataFrame()
                mood = "Error processing request"
                print(f"Error: {e}")
    
    # Example top rated movies for display
    top_rated_movies = movie_metadata.head(10)  # Replace with actual top-rated movie logic
    
    return render_template('index.html', recommendations=recommendations.to_dict(orient='records'), mood=mood, top_rated=top_rated_movies.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)