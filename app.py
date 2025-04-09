import streamlit as st
import pickle
import requests
import html

# Load and apply custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
                    st.image(poster, width=150)
                    st.markdown(f"<div class='card-title'>{clean_show}</div>", unsafe_allow_html=True)

