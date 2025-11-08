import streamlit as st

st.title("🧩 Énigme 4 – La grande finale 😈")
st.write("Si f(x) = x³ + 3x² + 3x + 1, quelle est **la dérivée de f(2x)** ?")

reponse = st.text_input("Ta réponse : (en Python par ex. 6x**2+12x+6)")
if st.button("Valider ma réponse ✅"):
    if reponse.replace(" ", "").lower() == "6x**2+12x+6":
        st.session_state.results[3] = True
        st.success("Bonne réponse ! 🎓 Pas de cadeau ici, juste le respect de Matteo 😎")
    else:
        st.session_state.results[3] = False
        st.warning("Pas tout à fait... mais bravo d’avoir tenté jusqu’au bout 🎅")
