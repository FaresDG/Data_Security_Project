import streamlit as st

# 1) Configuration de la page
st.set_page_config(page_title="Connexion", page_icon="🔐", layout="centered")

# 2) Votre CSS (idem)
st.markdown("""
    <style>
      body { background-color: #f5f7fa; }
      .login-container {
        background-color: white;
        padding: 2.5rem 2rem;
        border-radius: 12px;
        
        max-width: 400px;
        margin: 5vh auto 0;
        text-align: center;
        animation: fadeInUp 1s ease-out;
      }
      img {
        margin-bottom: 1.5rem;
        max-width: 100px;
        animation: fadeIn 1.2s ease-in;
      }
      .stTextInput > div > div > input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
      }
      .stButton button {
        background-color: #1e90ff;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        border: none;
        margin-top: 1.2rem;
        transition: background-color 0.3s ease, transform 0.2s ease;
      }
      .stButton button:hover {
        background-color: #1565c0;
        transform: scale(1.03);
      }
      @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
      }
      @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
      }
    </style>
""", unsafe_allow_html=True)

# 3) On ouvre UNE SEULE fois le conteneur
st.markdown('<div class="login-container">', unsafe_allow_html=True)

# 4) Tout votre contenu à l’intérieur
st.image("image3.jfif", use_container_width=False)
user_id  = st.text_input("ID")
password = st.text_input("Password", type="password")

if st.button("Se connecter"):
    if user_id=="admin" and password=="1234":
        st.success("✅ Connexion réussie !")
    else:
        st.error("❌ Identifiants incorrects.")

# 5) On ferme le div
st.markdown('</div>', unsafe_allow_html=True)
