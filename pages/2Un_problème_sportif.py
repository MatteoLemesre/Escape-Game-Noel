import streamlit as st

st.title("🧩 Énigme 2 — Le sport roi ⚽")
st.write("Après le Nord, restons dans le même thème avec le **LOSC** 🔴⚪.")
st.write("Cette fois, on parle du **monde du football international**.")

st.markdown("---")
st.write("**1ère question :** Qui a marqué un doublé en finale de la Coupe du Monde 1998 au Stade de France ? 🇫🇷")
st.write("**2ème question :** Qui a marqué un triplé en finale de la Coupe du Monde 2022 ? 🌍")
st.markdown("---")

st.write("💬 Le mot à trouver est **le club commun** de ces deux joueurs.")

if "enigme2_validee" not in st.session_state:
    st.session_state.enigme2_validee = False

if not st.session_state.enigme2_validee:
    rep = st.text_input("Ta réponse :").lower().replace(" ", "")
    if st.button("Valider ✅"):
        if rep in ['realmadrid', 'real', 'madrid']:
            st.session_state.gifts = st.session_state.get("gifts", []) + ["Un ballon de foot ⚽"]
            st.session_state.enigme2_validee = True
            st.success("🎉 Bravo ! Cadeau gagné : Un ballon de foot ⚽")
            st.balloons()
        else:
            st.error("❌ Mauvaise réponse... Essaie encore !")

else:
    st.success("✅ Énigme déjà validée ! Cadeau gagné : Un ballon de foot ⚽")

