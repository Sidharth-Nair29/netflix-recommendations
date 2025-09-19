import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv(r'C:\Users\comp\Desktop\netflix recommender\NetFlix.csv')
df = df.fillna('Unknown')
df['title'] = df['title'].str.strip().str.lower()

df['combined_cols'] = ((df['description'] + ' ') * 2 +(df['genres'] + ' ') * 5 +(df['cast'] + ' ') * 1 +(df['director'] + ' ') * 1).str.lower()

tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['combined_cols'])

# --- Cosine similarity ---
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Map titles to indices
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# --- Recommender function ---
def recommend(title, cosine_sim=cosine_sim):
    title = title.strip().lower()
    if title not in indices:
        return f"❌ '{title}' not found in dataset."

    idx = indices[title]
    input_type = df.iloc[idx]['type']

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]

    recommendations = []
    seen_descriptions = set()

    for i, score in sim_scores:
        if df['type'].iloc[i] == input_type:  # same type (Movie/TV Show)
            desc = df['description'].iloc[i]
            if desc not in seen_descriptions:  # skip duplicates
                seen_descriptions.add(desc)
                recommendations.append((df['title'].iloc[i], round(float(score), 2)))
        if len(recommendations) == 5:
            break

    return recommendations

# --- Streamlit UI ---
st.title("🎬 Netflix Recommendation System")
titles = df['title'].unique()
selected_title = st.selectbox("Choose a movie or show:", [t.title() for t in titles])

if st.button("Get Recommendations"):
    recommendations = recommend(selected_title)
    st.subheader("Recommended for you:")
    if isinstance(recommendations, str):
        st.error(recommendations)
    else:
        for r, score in recommendations:
            movie = df[df['title'] == r].head(1)
            if not movie.empty:
                movie = movie.iloc[0]
                st.markdown(f"**{movie['title'].title()}** ({movie['type']})")
                st.write(movie['description'])
                st.caption(f"Similarity Score: {score}")
                st.write("---")