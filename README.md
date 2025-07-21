# 🤖 Gerador Inteligente de Artigos para Blog

Este projeto é uma solução para o **Case 4: Gerador Inteligente de Artigos para Blog**, proposto no desafio técnico.

## 📝 Contexto do Desafio

O objetivo é atender à necessidade de uma agência de marketing digital que busca escalar a produção de conteúdo de qualidade para blogs, acelerando a criação de artigos sem perder a relevância e a personalização.

## 💡 A Solução

Para resolver o problema, foi desenvolvida uma aplicação que automatiza a criação de artigos utilizando uma equipe de agentes de Inteligência Artificial. A solução cumpre todos os requisitos do desafio:

**Geração Automática:** A partir de um único tema, o sistema gera um artigo completo e bem estruturado, com introdução, tópicos de desenvolvimento e conclusão.
**Seleção de Tom de Voz:** Permite que o usuário escolha o tom do texto (ex: Técnico, Informal, Persuasivo), garantindo que o conteúdo se alinhe à persona do blog.
**Sugestão de Títulos:** Ao final do processo, o sistema sugere pelo menos 3 títulos alternativos para o artigo gerado.

### ⚙️ Como Funciona?

O sistema foi construído em Python utilizando o framework **CrewAI** para orquestrar uma equipe de agentes de IA, cada um com uma função especializada:

1.  **Pesquisador:** Coleta informações e dados relevantes sobre o tema.
2.  **Estruturador:** Define a estrutura lógica do artigo.
3.  **Redator:** Escreve o conteúdo, seguindo a estrutura e o tom definidos.
4.  **Sugestor de Títulos:** Cria títulos criativos com base no conteúdo final.
5.  **Revisor:** Revisa, formata e entrega a versão final do artigo em Markdown.

### 🚀 Tecnologias Utilizadas

* **Linguagem:** Python
* **Orquestração de IA:** CrewAI & LangChain
* **Modelos de Linguagem:** OpenAI (via API)
* **Interface Web:** Streamlit
* **Ferramentas:** SerperDevTool para pesquisa em tempo real
