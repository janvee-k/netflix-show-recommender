Dataset used: https://www.kaggle.com/datasets/shivamb/netflix-shows/data

# netflix-show-recommender

This is a machine learning-powered web application built using Streamlit. The app recommends similar Netflix shows based on the user's input. It uses a cosine similarity model to suggest the most relevant recommendations, making it perfect for discovering new shows to watch. You can select a show from a dropdown menu, and the app will fetch and display a list of 10 similar shows along with their posters.


## How It Works
1. **Choose a show**: From the dropdown menu, select any Netflix show you'd like to get recommendations for.
2. **Click "Get Recommendations"**: Once you've selected your show, click the button to see a list of similar shows.
3. **Explore Recommendations**: The app will display up to 10 shows that are similar to the one you picked, complete with posters and titles.
4. **Cosine Similarity Model**: The model used to calculate recommendations (`cosine_sim.pkl`) is fetched from a Dropbox link to avoid file size restrictions on GitHub.
---

## Features

- **Easy-to-Use Interface**: The app is designed to be simple and interactive. Just choose a show, and you're ready to go!
- **Real-time Recommendations**: As soon as you click the button, you’ll get show recommendations based on your input.
- **Show Posters**: Each recommendation comes with a poster, making it visually appealing and easy to browse.

---

## Technologies Used
- **Streamlit**: Used to build the interactive web application.
- **Python**: The main programming language for the backend logic and recommendation system.
- **Cosine Similarity**: A mathematical method to measure the similarity between shows based on their features.
- **OMDb API**: To fetch posters of the shows for a better visual experience.
- **Dropbox**: Used to store the large `cosine_sim.pkl` file remotely to avoid GitHub's file size limitations.

---
## Installation & Usage

To run this project locally, follow the steps below:

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package manager)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/janvee-k/netflix-show-recommender.git
   ```

2. Navigate to the project folder:

  ```bash
  cd netflix-show-recommender
  ```

3. Create a virtual environment (optional but recommended):

  ```bash
    python -m venv venv
```

4. Activate the virtual environment:

- For Windows:

  ```bash
  .\venv\Scripts\activate
  ```
- For macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
5. Install the required dependencies:

  ```bash
  pip install -r requirements.txt
  ```
6. Run the app:

  ```bash
  streamlit run app.py
  ```
Your app will be available at http://localhost:8501 in your browser.

## File Structure

The repository structure is as follows:

netflix-show-recommender/ │ ├── app.py # Main Streamlit app ├── requirements.txt # List of Python dependencies ├── style.css # Custom CSS for styling the app ├── cosine_sim.pkl # Cosine similarity model ├── df.pkl # DataFrame containing Netflix shows ├── indices.pkl # Indices for the shows in the DataFrame └── README.md # Project description and instructions


## License
This project is licensed under the MIT License - see the LICENSE file for details.
