"""Módulos para adicionar escolha aleatória, delay e chamar as ferramentas do streamlit"""
import random
import time
import streamlit as st

st.title("Chat demo")

# Inicializa histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra mensagens do histórico quando o app restarta
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Recebendo input do usuário
if prompt := st.chat_input("Olá, tudo bem?"):
    # Mostra mensagens do usuário no container de mensagens do chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Mostra resposta do assistente no container de mensagens
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Olá! Como posso lhe ajudar hoje?",
                "Olá, humano! Posso ajudar em algo?",
                "Precisa de ajuda?",
            ]
        )

        # Simula delay de resposta
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Adicionando cursor simulando digitação
            message_placeholder.markdown(full_response +  "▌")
        message_placeholder.markdown(full_response)

    # Adiciona resposta do assistente no histórico do chat
    st.session_state.messages.append({"role": "assistant", "content": full_response})
