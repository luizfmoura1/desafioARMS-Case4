import streamlit as st
from main import run_blog_generator
import os

st.set_page_config(page_title="Gerador de Artigos com IA", layout="wide")

st.title("🤖 Gerador Inteligente de Artigos para Blog")
st.markdown("""
Esta aplicação utiliza um time de agentes de Inteligência Artificial para criar artigos de alta qualidade sobre qualquer tema.
Basta fornecer o tema, escolher o tom de voz e clicar em 'Gerar Artigo'.
""")

st.sidebar.header("Configurações do Artigo")
topic = st.sidebar.text_input("Qual é o tema do artigo?", "Inteligência Artificial em 2025")
tone = st.sidebar.selectbox(
    "Escolha o tom do texto:",
    ("Informal", "Técnico", "Persuasivo", "Informativo", "Instrutivo/Didático", "Irônico/Sarcástico", "Crítico")
)

if st.sidebar.button("Gerar Artigo 🚀"):
    if topic:
        st.info("Gerando seu artigo... Este processo pode levar alguns minutos. ⏳")
        
        with st.spinner('Pesquisando, escrevendo e revisando... Por favor, aguarde.'):
            try:
                final_article = run_blog_generator(topic, tone)
                
                st.success("Seu artigo foi gerado com sucesso! ✅")
                st.markdown("---")
                st.markdown(final_article)

                output_dir = "output"
                os.makedirs(output_dir, exist_ok=True)
                file_name = f"artigo_{topic.replace(' ', '_').lower()}.md"
                file_path = os.path.join(output_dir, file_name)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(final_article)
                
                st.sidebar.success(f"Artigo também salvo em `{file_path}`")

            except Exception as e:
                st.error(f"Ocorreu um erro ao gerar o artigo: {e}")
    else:
        st.warning("Por favor, insira um tema para o artigo.")
else:
    st.info("Preencha as configurações na barra lateral e clique no botão para começar.")