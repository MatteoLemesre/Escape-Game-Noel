# streamlit run "/Users/matteolemesre/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/Escape-Game-Noel/main.py"

import streamlit as st
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="Escape Game - La liste de Matteo", page_icon="🎁")

# --- INITIALISATION ---
if "step" not in st.session_state:
    st.session_state.step = 0
if "results" not in st.session_state:
    st.session_state.results = [None, None, None, None]
if "gifts" not in st.session_state:
    st.session_state.gifts = []
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

# --- INTRO ---
if st.session_state.step == 0:
    st.title("🎄 Escape Game – La Liste de Matteo 🎁")
    st.write("Bienvenue dans le **jeu de Noël de Matteo** ! 🌟")
    st.write("Ton objectif : **découvrir les cadeaux** de la liste de Matteo, en réussissant plusieurs énigmes.")
    st.write("Chaque énigme te fait gagner un cadeau 🎁 … sauf la dernière, qui testera juste ton intelligence 👀.")
    st.write("⚠️ Trois mauvaises réponses = le cadeau disparaît à jamais.")
    st.divider()

    noms_possibles = ["Sonia", "Juliette", "Camille L.", "Camille", "Stéphane", "Sven", "Corentin", "Autre..."]
    choix = st.selectbox("Choisis ton nom :", noms_possibles)
    if choix == "Autre...":
        st.session_state.player_name = st.text_input("Entre ton prénom :", key="nom_perso")
    else:
        st.session_state.player_name = choix

    if st.button("🎁 Commencer l’aventure") and st.session_state.player_name.strip():
        st.session_state.step = 1

# --- LISTE DES ÉNIGMES ---
enigmes = [
    {
        "intro": "Première mission, facile pour s’échauffer 🧩",
        "texte": "Quelle couleur obtient-on en mélangeant **le bleu et le jaune** ?",
        "answer": "vert",
        "cadeau": "Un pull de Noël 🎅"
    },
    {
        "intro": "On monte d’un cran... un peu de calcul mental 🧠",
        "texte": "Quelle est **la somme des chiffres de 2025** ?",
        "answer": "9",
        "cadeau": "Des chocolats 🍫"
    },
    {
        "intro": "Petit clin d’œil à ma passion 📊",
        "texte": "Dans le mot **DATA**, combien de lettres sont identiques ?",
        "answer": "2",
        "cadeau": "Un livre de Data Science 📘"
    },
    {
        "intro": "La grande finale. Seuls les plus courageux s’y aventurent 😈",
        "texte": "Si f(x) = x³ + 3x² + 3x + 1, quelle est **la dérivée de f(2x)** ?",
        "answer": "6x**2+12x+6",
        "cadeau": None
    }
]

# --- JEU ---
if st.session_state.step > 0 and st.session_state.step <= len(enigmes):
    st.title("🎄 Escape Game – La Liste de Matteo 🎁")
    
    # Bloc récapitulatif
    st.markdown("---")
    st.subheader("📋 Progression du jeu")
    for i, r in enumerate(st.session_state.results):
        if r is None:
            st.write(f"Énigme {i+1} : ⏳ Pas encore jouée")
        elif r:
            st.write(f"✅ Énigme {i+1} : Validée – Cadeau : {enigmes[i]['cadeau']}")
        else:
            st.write(f"❌ Énigme {i+1} : Perdue – Matteo est déçu 🥲")

    # Ligne de séparation
    st.markdown("---")

    # Enigme actuelle
    index = st.session_state.step - 1
    e = enigmes[index]
    st.subheader(f"🧩 Énigme {index+1}")
    st.write(f"*{e['intro']}*")
    st.write(e["texte"])
    
    reponse = st.text_input("Ta réponse :", key=f"rep_{index}")
    if f"tries_{index}" not in st.session_state:
        st.session_state[f"tries_{index}"] = 0

    if st.button("Valider ma réponse ✅", key=f"btn_{index}"):
        st.session_state[f"tries_{index}"] += 1
        cleaned = reponse.lower().replace(" ", "")
        if cleaned == e["answer"].lower().replace(" ", ""):
            st.session_state.results[index] = True
            if e["cadeau"]:
                st.session_state.gifts.append(e["cadeau"])
                st.success(f"🎉 Bonne réponse ! Cadeau gagné : {e['cadeau']}")
            else:
                st.info(f"Bonne réponse, merci ChatGPT... pardon *{st.session_state.player_name}* 😅 Mais cette question était sans cadeau final 🎁")
            st.session_state.step += 1
        else:
            if st.session_state[f"tries_{index}"] >= 3 and e["cadeau"]:
                st.session_state.results[index] = False
                st.error("💀 Trois erreurs... Cadeau perdu à jamais !")
                st.session_state.step += 1
            elif not e["cadeau"]:
                st.session_state.results[index] = False
                st.warning("Mauvaise réponse, mais merci d’avoir tenté l’ultime épreuve ! Cette question n’offrait pas de cadeau 🎁")
                st.session_state.step += 1
            else:
                st.warning(f"Mauvaise réponse... (tentative {st.session_state[f'tries_{index}']}/3)")

# --- FIN DU JEU ---
if st.session_state.step > len(enigmes):
    st.title("🎄 Escape Game – La Liste de Matteo 🎁")
    st.markdown("---")
    st.subheader("🎉 Fin de l’aventure !")
    st.write(f"Merci d’avoir joué jusqu’au bout, {st.session_state.player_name} 🙌")

    if st.session_state.gifts:
        st.success("🎁 Voici les cadeaux que tu as découverts :")
        for g in st.session_state.gifts:
            st.write(f"- {g}")
    else:
        st.write("😅 Aucun cadeau trouvé… mais l’esprit de Noël est en toi 🎅")

    st.markdown("---")
    if st.button("📩 Envoyer les résultats à Matteo"):
        message = f"""
        Joueur : {st.session_state.player_name}
        Résultats : {st.session_state.results}
        Cadeaux trouvés : {', '.join(st.session_state.gifts) if st.session_state.gifts else 'Aucun'}
        """

        try:
            EMAIL_SENDER = "matteo.lemesre2@gmail.com"
            EMAIL_PASSWORD = ""  # ton mot de passe d’application ici
            EMAIL_RECEIVER = "matteo.lemesre2@gmail.com"

            msg = MIMEText(message)
            msg["Subject"] = f"Résultats Escape Game - {st.session_state.player_name}"
            msg["From"] = EMAIL_SENDER
            msg["To"] = EMAIL_RECEIVER

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.send_message(msg)

            st.success("✅ Résultats envoyés à Matteo avec succès !")
        except Exception as e:
            st.error("❌ Erreur lors de l’envoi de l’e-mail (pense à ajouter ton mot de passe d’application)")

