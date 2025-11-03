import streamlit as st
import smtplib
from email.mime.text import MIMEText

# 🎅 Configuration
st.set_page_config(page_title="Le Jeu de Matteo 🎄", page_icon="🎁", layout="centered")

# --------------------------
# ⚙️ INITIALISATION
# --------------------------
if "step" not in st.session_state:
    st.session_state.step = 0  # étape du jeu
if "results" not in st.session_state:
    st.session_state.results = [None, None, None, None]  # état de chaque énigme
if "gifts" not in st.session_state:
    st.session_state.gifts = []
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

# --------------------------
# 🎄 ÉTAPE 0 : INTRO
# --------------------------
if st.session_state.step == 0:
    st.title("🎅 Le Jeu de Matteo 🎄")
    st.write("Bienvenue dans le jeu de Noël de Matteo ! Résous les énigmes pour découvrir les cadeaux mystères 🎁.")
    st.write("⚠️ Attention : trois mauvaises réponses sur une énigme et tu perds le cadeau correspondant.")
    st.divider()

    # Choix du joueur
    noms_possibles = ["Camille", "Alex", "Théo", "Lucie", "Autre..."]
    choix = st.selectbox("Choisis ton nom dans la liste :", noms_possibles)
    if choix == "Autre...":
        st.session_state.player_name = st.text_input("Entre ton prénom :", key="nom_personnalise")
    else:
        st.session_state.player_name = choix

    if st.button("Commencer le jeu 🎁") and st.session_state.player_name.strip():
        st.session_state.step = 1
        st.experimental_rerun()

# --------------------------
# 🧩 LISTE DES ÉNIGMES
# --------------------------
enigmes = [
    {
        "texte": "1️⃣ Quelle couleur obtient-on en mélangeant le bleu et le jaune ?",
        "answer": "vert",
        "cadeau": "Un pull de Noël 🎅"
    },
    {
        "texte": "2️⃣ Quelle est la somme des chiffres de 2025 ?",
        "answer": "9",
        "cadeau": "Des chocolats 🍫"
    },
    {
        "texte": "3️⃣ Dans le mot 'DATA', combien de lettres sont identiques ?",
        "answer": "2",
        "cadeau": "Un livre de Data Science 📘"
    },
    {
        "texte": "4️⃣ (Énigme finale 😈) Si f(x) = x³ + 3x² + 3x + 1, quelle est la dérivée de f(2x) ?",
        "answer": "6x**2+12x+6",  # réponse symbolique attendue
        "cadeau": None  # pas de cadeau
    }
]

# --------------------------
# 🎯 GESTION DES ÉNIGMES
# --------------------------
if st.session_state.step > 0 and st.session_state.step <= len(enigmes):
    index = st.session_state.step - 1
    e = enigmes[index]
    st.subheader(f"Énigme {index+1}")
    st.write(e["texte"])
    
    reponse = st.text_input("Ta réponse :", key=f"reponse_{index}")
    if f"tries_{index}" not in st.session_state:
        st.session_state[f"tries_{index}"] = 0

    if st.button("Valider", key=f"valider_{index}"):
        st.session_state[f"tries_{index}"] += 1
        if reponse.lower().replace(" ", "") == e["answer"].lower().replace(" ", ""):
            if index < 3:  # Pour les 3 premiers cadeaux
                st.session_state.results[index] = True
                st.session_state.gifts.append(e["cadeau"])
                st.success(f"Bonne réponse 🎉 Cadeau gagné : {e['cadeau']}")
            else:
                st.session_state.results[index] = True
                st.info(f"Bonne réponse, merci ChatGPT... pardon *{st.session_state.player_name}* 😅 Mais cette question était sans cadeau final 🎁")
            st.session_state.step += 1
            st.experimental_rerun()
        else:
            if st.session_state[f"tries_{index}"] >= 3 and index < 3:
                st.session_state.results[index] = False
                st.error("Trop d'erreurs 😢 Cadeau perdu...")
                st.session_state.step += 1
                st.experimental_rerun()
            elif index == 3:
                st.session_state.results[index] = False
                st.warning("Mauvaise réponse, mais merci d'avoir joué jusqu'au bout ! Cette question, trop dure, n'apportait pas de cadeau 🎁")
                st.session_state.step += 1
                st.experimental_rerun()
            else:
                st.warning(f"Mauvaise réponse... (tentative {st.session_state[f'tries_{index}']}/3)")

# --------------------------
# 🧾 AFFICHAGE DES RÉSULTATS INTERMÉDIAIRES
# --------------------------
if any(r is not None for r in st.session_state.results):
    st.divider()
    st.subheader("📋 Résultats intermédiaires :")
    for i, r in enumerate(st.session_state.results):
        if r is None:
            st.write(f"Énigme {i+1} : ⏳ Pas encore jouée")
        elif r:
            cadeau = enigmes[i]["cadeau"]
            if cadeau:
                st.write(f"✅ Énigme {i+1} : Validé - Cadeau : {cadeau}")
            else:
                st.write(f"✅ Énigme {i+1} : Bonne réponse (pas de cadeau pour celle-ci)")
        else:
            st.write(f"❌ Énigme {i+1} : Faux - Matteo est déçu 😢")

# --------------------------
# 🎉 ÉTAPE FINALE
# --------------------------
if st.session_state.step > len(enigmes):
    st.divider()
    st.success(f"🎄 Merci d’avoir joué jusqu’au bout, {st.session_state.player_name} !")
    if st.session_state.gifts:
        st.write("🎁 Tu as gagné :")
        for g in st.session_state.gifts:
            st.write(f"- {g}")
    else:
        st.write("😅 Tu n’as rien gagné... mais l’esprit de Noël est en toi 🎅")

    # Bouton final
    if st.button("Finir le jeu et envoyer les résultats 📩"):
        # 📨 Envoi des résultats par e-mail (à configurer)
        message = f"""
        Joueur : {st.session_state.player_name}
        Résultats :
        {st.session_state.results}
        Cadeaux gagnés : {', '.join(st.session_state.gifts) if st.session_state.gifts else 'Aucun'}
        """

        try:
            # ⚠️ À configurer : ton adresse e-mail + mot de passe d’application
            EMAIL_SENDER = "ton_adresse@gmail.com"
            EMAIL_PASSWORD = "mot_de_passe_app"
            EMAIL_RECEIVER = "ton_adresse@gmail.com"

            msg = MIMEText(message)
            msg["Subject"] = f"Résultats du jeu de Noël - {st.session_state.player_name}"
            msg["From"] = EMAIL_SENDER
            msg["To"] = EMAIL_RECEIVER

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.send_message(msg)
            
            st.success("📧 Résultats envoyés avec succès à Matteo !")
        except Exception as e:
            st.error("Erreur lors de l’envoi de l’e-mail (à configurer manuellement)")
            st.text(str(e))
