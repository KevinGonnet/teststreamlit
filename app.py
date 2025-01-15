import streamlit as st

# Titre de l'app
st.title("Hello Streamlit!")

# Entrée utilisateur
user_input = st.text_input("Entrez un texte :")

# Affichage de la réponse
if user_input:
    st.write(f"Vous avez écrit : {user_input}")
