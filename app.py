import streamlit as st
from src.recommender import recommend

st.title("🎌 NakamaAI Chat Recommender")

# Session state
if "stage" not in st.session_state:
    st.session_state.stage = 0

if "favorite" not in st.session_state:
    st.session_state.favorite = ""

if "genres" not in st.session_state:
    st.session_state.genres = ""

# Initial bot message
if st.session_state.stage == 0:
    st.write("Bot: Hey! Let's find you some anime.")
    st.write("Bot: What's one of your favorite anime?")
    st.session_state.stage = 1

user_input = st.chat_input("Type here...")

if user_input:

    st.write("You:", user_input)

    # Stage 1 → Favorite anime
    if st.session_state.stage == 1:

        st.session_state.favorite = user_input

        recs = recommend(user_input)

        if recs is None:
            st.write("Bot: Mmm... I couldn't find that anime.")
            st.write("Bot: Could you try the alternate Japanese title?")
            st.write("Example: Shingeki no Kyojin instead of Attack on Titan.")
        else:
            st.write("Bot: Nice choice! What genres do you usually enjoy?")
            st.session_state.stage = 2

    # Stage 2 → Genre preference
    elif st.session_state.stage == 2:

        st.session_state.genres = user_input

        st.write("Bot: Got it. Generating recommendations...")

        recs = recommend(st.session_state.favorite)

        st.write("### 🎯 Recommended Anime")

        for r in recs:
            st.write("•", r)

        st.write("Bot: Want more recommendations? Refresh the page and try again!")