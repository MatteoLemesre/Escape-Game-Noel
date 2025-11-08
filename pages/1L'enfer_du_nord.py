import streamlit as st

st.title("🧩 Énigme 1")
st.write("Vous n'étes pas sans savoir que ma region d'origine est importante pour moi: Le Nord.")
st.write("Dans ce jeu, vous allez devoir trouvé un mot composé des premières lettres des reponses aux différentes questions.")
st.write("1ère Question: Il est l'élement essentiel de la spécialité du Nord, le Welsh.")
st.write("2ème Question: ")

if "enigme1_validee" not in st.session_state:
    st.session_state.enigme1_validee = False

if not st.session_state.enigme1_validee:
    rep = st.text_input("Ta réponse :")
    if st.button("Valider"):
        if rep.lower().replace(" ", "") == "vert":
            st.session_state.gifts = st.session_state.get("gifts", []) + ["Un pull de Noël 🎅"]
            st.session_state.enigme1_validee = True
            st.success("Bravo ! Cadeau gagné : Un pull de Noël 🎅")
        else:
            st.error("Mauvaise réponse...")
