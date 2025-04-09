import streamlit as st
import pickle
import requests

# Dropbox shared link
dropbox_link = 'https://www.dropbox.com/scl/fi/aun6ellbthtk06bsvu1q8/cosine_sim.pkl?rlkey=4lyuniz50mg267z1mj9m2x1nd&dl=0'  # `dl=1` forces the file to download

# Function to download the file from Dropbox
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded: {filename}")

# Download cosine_sim.pkl file from Dropbox
download_file(dropbox_link, 'cosine_sim.pkl')

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
