# netflix-show-recommender

This is a machine learning-powered web application built using Streamlit. The app recommends similar Netflix shows based on the user's input. It uses a cosine similarity model to suggest the most relevant recommendations, making it perfect for discovering new shows to watch. You can select a show from a dropdown menu, and the app will fetch and display a list of 10 similar shows along with their posters.

Dataset used: https://www.kaggle.com/datasets/shivamb/netflix-shows/data


## How It Works

1. **Choose a show**: Select a Netflix show from the dropdown menu.
2. **Get Recommendations**: Click the button to view a list of similar shows.
3. **View Results**: The app displays up to 10 shows similar to your selection, with posters and titles.
4. **Recommendation Model**: The recommendations are based on cosine similarity and are fetched using a precomputed model hosted on Dropbox.

---

## Features

- **Interactive Interface**: Built with Streamlit for a fast and user-friendly experience.
- **Visual Output**: Show posters are displayed alongside recommendations for an improved UI.
- **Dynamic Model Loading**: The cosine similarity model is automatically downloaded from Dropbox if not available locally.
- **Title Matching**: Automatically handles and cleans titles with special characters.

---

## Technologies Used

- **Streamlit** – For building the web application.
- **Python** – Core programming language used for logic and backend.
- **Cosine Similarity** – For computing show similarity.
- **OMDb API** – For fetching posters and metadata.
- **Dropbox** – To host and serve the large precomputed cosine similarity model file.

---

## Installation and Usage

Follow the steps below to run the project locally:

```bash```
# 1. Clone the repository
git clone https://github.com/janvee-k/netflix-show-recommender.git

# 2. Navigate to the project directory
cd netflix-show-recommender

# 3. (Optional) Create and activate a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 4. Install the dependencies
pip install -r requirements.txt

# 5. Run the Streamlit app
streamlit run app.py

# 6. The app will open in your browser at http://localhost:8501

## Project Structure:

netflix-show-recommender/
├── app.py                         # Main application code
├── cosine_sim.pkl                # Cosine similarity matrix (downloaded if not present)
├── df.pkl                        # DataFrame with show features
├── indices.pkl                   # Index mapping for show titles
├── netflix_titles.csv            # Original dataset from Kaggle
├── requirements.txt              # Required Python packages
├── style.css                     # Custom styles for Streamlit app
├── netflix-recommender-preview.png  # App preview image
├── LICENSE                       # License file
└── README.md                     # Project documentation


## License
This project is licensed under the MIT License - see the LICENSE file for details.
