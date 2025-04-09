# netflix-show-recommender

This is a machine learning-powered web application built using Streamlit. The app recommends similar Netflix shows based on the user's input. It uses a cosine similarity model to suggest the most relevant recommendations, making it perfect for discovering new shows to watch. You can select a show from a dropdown menu, and the app will fetch and display a list of 10 similar shows along with their posters.

## How It Works

1. **Choose a show**: From the dropdown menu, select any Netflix show you'd like to get recommendations for.
2. **Click "Get Recommendations"**: Once you've selected your show, click the button to see a list of similar shows.
3. **Explore Recommendations**: The app will display up to 10 shows that are similar to the one you picked, complete with posters and titles.

## Features

- **Easy-to-Use Interface**: The app is designed to be simple and interactive. Just choose a show, and you're ready to go!
- **Real-time Recommendations**: As soon as you click the button, you’ll get show recommendations based on your input.
- **Show Posters**: Each recommendation comes with a poster, making it visually appealing and easy to browse.

## Technologies Used

- **Streamlit**: Used to build the interactive web application.
- **Python**: The main programming language for the backend logic and recommendation system.
- **Cosine Similarity**: A mathematical method to measure the similarity between shows based on their features.
- **OMDb API**: To fetch posters of the shows for a better visual experience.
