import requests


# Base URL for the API
BASE_URL = "https://opentdb.com/api.php?amount=10&type=boolean"
# Function to fetch trivia questions
def fetch_trivia_questions():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data['results']
    except requests.RequestException as e:
        print(f"Error fetching trivia questions: {e}")
        return []

question_data = fetch_trivia_questions()