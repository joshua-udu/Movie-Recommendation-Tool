# Movie Recommendation System

## Overview

This Movie Recommendation System suggests movies based on user input and viewing history. It uses sentiment analysis to understand the user's mood and recommends movies accordingly. It also integrates user-based collaborative filtering and item-based similarity to provide personalized recommendations.

## Features

- **User-Based Recommendations:** Provides movie suggestions based on user preferences and viewing history.
- **Emotion-Based Recommendations:** Suggests movies based on the user's mood detected from their input.
- **Top Rated Movies:** Displays a list of top-rated movies for general recommendations.

## Requirements

- **Python 3.8+**
- **Flask**
- **Pandas**
- **NLTK**
- **Scikit-learn**
- **Surprise (for collaborative filtering)**

## Data

### Required Data Files

1. **Viewing History (`viewing_history.csv`)**
   - **Columns:** `user_id`, `movie_id`, `rating`
   - **Description:** Historical data of users' movie ratings.

2. **Movie Metadata (`movie_metadata.csv`)**
   - **Columns:** `movie_id`, `title`, `genre`
   - **Description:** Information about movies including their titles and genres.

### Sample Data

You can use the sample data provided in the `data/` directory, or create your own based on the structure described above.

## Setup

### Install Dependencies

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Create `requirements.txt`

```txt
Flask==2.2.3
pandas==2.1.0
nltk==3.8.1
scikit-learn==1.2.1
surprise==0.1.1
```

## Setup Instructions

1. **Place Your Data Files:**

   Ensure that `viewing_history.csv` and `movie_metadata.csv` are placed in the `data/` directory.

2. **Update Configuration (if needed):**

   Modify `app/main.py` to point to your data files if they are in a different location.

3. **Run the Application:**

   Start the Flask application:

   ```bash
   python app/main.py
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Access the Web Interface:**

   Open a web browser and go to `http://127.0.0.1:5000/`.

2. **Provide User Input:**

   - **User ID:** Enter the ID of the user for whom you want recommendations.
   - **User Input:** Enter text to analyze the mood. This could be a review, feedback, or any other text.

3. **View Recommendations:**

   The system will display:
   - **Personalized Recommendations:** Based on the user’s viewing history and mood.
   - **Top Rated Movies:** A list of top-rated movies for general suggestions.
   - **Detected Mood:** The mood extracted from the user input.

## Detailed Explanation

### Code Components

- **`app/main.py`**: Main Flask application file. Handles HTTP requests and serves the web interface.
- **`src/data_preparation.py`**: Contains functions to load and prepare data.
- **`src/model_filtering.py`**: Contains functions for training models and computing item similarities.
- **`src/recommendation_engine.py`**: Contains functions for generating recommendations based on user data and mood.
- **`src/sentiment_analysis.py`**: Contains functions for analyzing sentiment and mood.

### Sentiment Analysis

The `analyze_sentiment` function uses the VADER sentiment analysis tool to classify the mood of the user input. It currently categorizes text into **positive**, **negative**, or **neutral**. You can extend this to detect more emotions if needed.

### Recommendations

- **User-Based Recommendations:** Generated using collaborative filtering based on user ratings.
- **Emotion-Based Recommendations:** Adjusted based on the detected mood. For example, **positive** moods might get **Comedy** or **Action** suggestions, while **negative** moods might receive **Drama** or **Romance** suggestions.
