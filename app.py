import streamlit as st
import pickle
import requests
import zipfile
import os

# Function to unzip the cosine_sim.pkl.zip file
def unzip_model():
    with zipfile.ZipFile("cosine_sim.pkl.zip", 'r') as zip_ref:
        zip_ref.extractall()

# Load and apply custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Unzip the model files if they are not already unzipped
if not os.path.exists("cosine_sim.pkl"):
    unzip_model()

# Load models and data
try:
    cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
    indices = pickle.load(open('indices.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# Recommendation function
def recommend(title):
    title = title.lower()
    if title not in indices:
        st.warning("Sorry, we couldn't find that show.")
        return []
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_matches = sim_scores[1:11]  # Exclude the selected show itself
    top_indices = [i[0] for i in top_matches]
    
    return df['title'].iloc[top_indices].tolist()

# Function to fetch movie/show poster from OMDb API
def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey=thewdb"
    response = requests.get(url)
    data = response.json()
    return data.get('Poster', 'https://via.placeholder.com/150')

# Streamlit UI
st.title("🎬 Netflix Show Recommender")

selected_title = st.selectbox("Choose a show:", sorted(df['title'].unique()))

if st.button("Get Recommendations"):
    with st.spinner("Fetching recommendations..."):
        recommendations = recommend(selected_title)
        
    if recommendations:
        st.subheader("Recommended Shows:")
        
        # Display recommendations in a grid of cards (5 per row)
        num_columns = 5
        cols = st.columns(num_columns)  # Create 5 columns

        # Iterate over recommendations and display them in the grid
        for i, show in enumerate(recommendations):
            poster = fetch_poster(show)
            col = cols[i % num_columns]  # Distribute the shows across columns
            with col:
                st.image(poster, width=150)
                st.write(show)
