import streamlit as st
import pickle
import requests
import html
import os

# Load and apply custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Function to download cosine_sim.pkl from Dropbox
def download_cosine_sim():
    if not os.path.exists('cosine_sim.pkl'):
        st.info("Downloading similarity model... This may take a moment.")
        try:
            # Your Dropbox link with dl=1 for direct download
            url = "https://www.dropbox.com/scl/fi/aun6ellbthtk06bsvu1q8/cosine_sim.pkl?rlkey=4lyuniz50mg267z1mj9m2x1nd&dl=1"
            
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            
            with open('cosine_sim.pkl', 'wb') as f:
                f.write(response.content)
            
            st.success("Model downloaded successfully!")
        except Exception as e:
            st.error(f"Error downloading cosine_sim.pkl: {e}")
            st.stop()

# Download the model if it doesn't exist
download_cosine_sim()

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

# Clean title function to handle special characters
def clean_title(title):
    # Remove any '#' characters that might be in the title
    return title.replace('#', '').strip()

# Streamlit UI
st.title("🎬 Netflix Show Recommender")

# Get sorted list of unique titles and clean them
clean_titles = [clean_title(title) for title in df['title'].unique()]
sorted_titles = sorted(clean_titles)

selected_title = st.selectbox("Choose a show:", sorted_titles)

if st.button("Get Recommendations"):
    with st.spinner("Fetching recommendations..."):
        recommendations = recommend(selected_title)
        
    if recommendations:
        st.subheader("Recommended Shows:")
        
        # Create rows of 5 cards each
        # Process recommendations in chunks of 5
        for i in range(0, len(recommendations), 5):
            # Create a row with 5 columns
            cols = st.columns(5)
            
            # Fill each column with a card
            for col_idx, show_idx in enumerate(range(i, min(i+5, len(recommendations)))):
                show = recommendations[show_idx]
                clean_show = clean_title(show)
                poster = fetch_poster(clean_show)
                
                with cols[col_idx]:
                    # Use HTML div to force center alignment
                    st.markdown(f"""
                        <div style="text-align: center; display: flex; flex-direction: column; align-items: center;">
                            <img src="{poster}" style="width: 150px; height: 225px; object-fit: cover; border: 2px solid white; border-radius: 10px; margin-bottom: 10px;">
                            <p style="color: white; font-weight: 600; font-size: 14px; text-align: center; margin: 0; padding: 0 5px; line-height: 1.3;">{clean_show}</p>
                        </div>
                    """, unsafe_allow_html=True)
