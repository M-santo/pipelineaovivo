import streamlit as st
import contrato
from datetime import datetime, time
import re

# Função para validar o formato do email
def validar_email(email):
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(padrao_email, email):
        return True
    return False

def main():

    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0) ) # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZpFlow com Gemini", "ZapFlow com chatGPT",])

    if st.button("Salvar"):

        data_hora = datetime.combine(data, hora)
        st.write("**Dados da Venda:**")
        st.write(f"Email do vendedor: {email}")
        st.write(f"Data e Hora da Compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")

if __name__=="__main__":
    main()