from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from crewai_tools import SerperDevTool

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini",
                 temperature=0.7,
                 openai_api_key=os.getenv("OPENAI_API_KEY"))

search_tool = SerperDevTool()

class BlogAgents:
    def researcher_agent(self):
        return Agent(
            role='Pesquisador de Tema',
            goal='Coletar informações abrangentes e detalhadas sobre um tema específico para um artigo de blog, utilizando ferramentas de busca na internet.',
            backstory="Responsável por vasculhar fontes e compilar dados relevantes para embasar o conteúdo.",
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm
        )

    def article_structurer_agent(self):
        return Agent(
            role='Estruturador de Artigo',
            goal='Definir uma estrutura lógica e envolvente para o artigo de blog, incluindo introdução, tópicos principais e conclusão.',
            backstory="Especialista em organizar informações de forma que fluam bem e prendam a atenção do leitor.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def content_writer_agent(self):
        return Agent(
            role='Redator de Conteúdo',
            goal='Escrever seções do artigo de blog com base na estrutura e informações fornecidas, aderindo ao tom de voz especificado.',
            backstory="Um escritor criativo e adaptável, capaz de moldar o texto para diferentes públicos e propósitos.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def title_suggester_agent(self):
        return Agent(
            role='Sugestor de Títulos Criativos',
            goal='Gerar múltiplos títulos atraentes e otimizados para um artigo de blog.',
            backstory="Possui um talento especial para criar títulos que capturam a essência do conteúdo e atraem cliques.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    
    def reviser_formatter_agent(self):
        return Agent(
            role='Revisor e Formatador de Artigo',
            goal='Revisar o artigo de blog finalizado para corrigir erros gramaticais e de digitação, garantir a coesão e a clareza do texto, e formatar o conteúdo em Markdown para uma apresentação limpa e profissional.',
            backstory="Um perfeccionista com um olhar aguçado para detalhes, especializado em polir textos para publicação, garantindo que a qualidade final seja impecável e a leitura agradável.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )