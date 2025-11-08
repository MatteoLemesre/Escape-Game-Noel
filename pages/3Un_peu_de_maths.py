import streamlit as st

st.title("🧩 Énigme 3")
st.write("*Petit clin d’œil à ma passion 📊*")
st.write("Dans le mot **DATA**, combien de lettres sont identiques ?")

reponse = st.text_input("Ta réponse :")
if st.button("Valider ma réponse ✅"):
    if reponse.strip() == "2":
        st.session_state.gifts.append("Un livre de Data Science 📘")
        st.session_state.results[2] = True
        st.success("🎉 Bonne réponse ! Cadeau gagné : Un livre de Data Science 📘")
    else:
        st.session_state.results[2] = False
        st.error("Mauvaise réponse... Cadeau perdu 😢")
