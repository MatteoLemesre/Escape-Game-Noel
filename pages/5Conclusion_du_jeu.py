import streamlit as st
import smtplib
from email.mime.text import MIMEText

st.title("🎉 Fin de l’aventure !")

player = st.session_state.get("player_name", "Joueur anonyme")
results = st.session_state.get("results", [])
gifts = st.session_state.get("gifts", [])

if gifts:
    st.success("🎁 Voici les cadeaux que tu as découverts :")
    for g in gifts:
        st.write(f"- {g}")
else:
    st.info("😅 Aucun cadeau trouvé… mais l’esprit de Noël est en toi 🎅")

st.divider()

if st.button("📩 Envoyer mes résultats à Matteo"):
    message = f"""
🎄 Résultats Escape Game de Noël 🎁
Joueur : {player}

Résultats :
{results}

Cadeaux gagnés :
{', '.join(gifts) if gifts else 'Aucun 😢'}
"""

    EMAIL_SENDER = "matteo.lemesre2@gmail.com"
    EMAIL_PASSWORD = ""  # mot de passe d’application ici
    EMAIL_RECEIVER = "matteo.lemesre2@gmail.com"

    msg = MIMEText(message)
    msg["Subject"] = f"Résultats Escape Game - {player}"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        st.success("✅ Résultats envoyés à Matteo avec succès !")
    except Exception as e:
        st.error(f"❌ Erreur lors de l’envoi : {e}")
