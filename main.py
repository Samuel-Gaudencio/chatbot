import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("key"))


def app():
    st.header("Stream Chat", divider=True)
    st.write("Faça sua pergunta")
    
    msg_user = st.chat_input(placeholder="Peça ao Stream Chat")
    
    if "mensagens" not in st.session_state:
        st.session_state["mensagens"] = []

    if msg_user:
        st.session_state["mensagens"].append({"usuario": "user", "texto": msg_user})
        response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=f'{msg_user}'
                    )       
        st.session_state["mensagens"].append({"usuario": "assistant", "texto": response.text})
    
    
    for mensagem in st.session_state["mensagens"]:
        with st.chat_message(mensagem["usuario"]):
            st.write(mensagem["texto"])
    
app()



