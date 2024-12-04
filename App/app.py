#Importando minhas bibliotecas
import requests
import streamlit as st


#Criando função para retorno das músicas
def buscar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra

#******************************************************************************#
#Construção da minha interface
st.image("https://i.imgur.com/SmktDIH.png")
st.title("Letras de músicas")

banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar: ")
#******************************************************************************#


if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Encontramos a letra da sua música!")
        st.text(letra)
    else:
        st.error("Infelizmene não foi possível encontrar a letra dessa música")

