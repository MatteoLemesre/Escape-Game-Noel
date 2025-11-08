# streamlit run "/Users/matteolemesre/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/Escape-Game-Noel/Introduction.py"

import streamlit as st

st.set_page_config(page_title="Mini Escape Game - La liste de Matteo", page_icon="🎁")

if "player_name" not in st.session_state:
    st.session_state.player_name = ""
if "gifts" not in st.session_state:
    st.session_state.gifts = []
if "results" not in st.session_state:
    st.session_state.results = [None, None, None, None]

st.title("🎄 Mini Escape Game – La Liste de Matteo 🎁")
st.write("Bienvenue dans le **jeu de Noël de Matteo** ! 🌟")
st.write("Ton objectif : **découvrir les cadeaux** de la liste, en réussissant plusieurs énigmes.")
st.write("Chaque énigme te fait gagner un cadeau 🎁 … sauf la dernière, qui testera juste ton intelligence 👀.")
st.divider()

noms_possibles = ["Sonia", "Juliette", "Camille L.", "Camille", "Stéphane", "Sven", "Corentin", "Autre..."]
choix = st.selectbox("Choisis ton nom :", noms_possibles, index=None, placeholder="➡️ Sélectionne ton prénom")

if choix == "Autre...":
    player_name = st.text_input("Entre ton prénom :").strip()
elif choix:
    player_name = choix
else:
    player_name = ""

st.session_state.player_name = player_name

if player_name:
    st.success(f"Bienvenue {player_name} ! 🌟")
    st.info("Utilise le menu à gauche pour accéder à l’Énigme 1 ➡️")
else:
    st.warning("Entre ton prénom avant de commencer 🎅")