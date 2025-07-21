from crewai import Crew, Process
from src.agents import BlogAgents
from src.tasks import BlogTasks
import sys

def run_blog_generator(topic: str, tone: str):
    agents = BlogAgents()
    tasks = BlogTasks()

    researcher = agents.researcher_agent()
    structurer = agents.article_structurer_agent()
    writer = agents.content_writer_agent()
    title_suggester = agents.title_suggester_agent()


    research_task = tasks.research_task(researcher, topic)
    structure_task = tasks.structure_task(structurer, research_task, topic)
    write_content_task = tasks.write_content_task(writer, structure_task, research_task, topic, tone)
    suggest_titles_task = tasks.suggest_titles_task(title_suggester, write_content_task, topic)

    blog_crew = Crew(
        agents=[researcher, structurer, writer, title_suggester],
        tasks=[research_task, structure_task, write_content_task, suggest_titles_task],
        verbose=True,
        process=Process.sequential
    )

    print("#### Iniciando o processo de geração do artigo... ####")
    result = blog_crew.kickoff()
    print("\n#### Processo Concluído! ####\n")


    final_article = blog_crew.tasks_outputs[write_content_task.description] 
    suggested_titles = blog_crew.tasks_outputs[suggest_titles_task.description] 

    print("\n--- Artigo Gerado ---")
    print(final_article)
    print("\n--- Títulos Sugeridos ---")
    print(suggested_titles)

    with open(f"artigo_{topic.replace(' ', '_').lower()}.md", "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n")
        f.write(final_article)
        f.write("\n\n--- Títulos Alternativos ---\n")
        f.write(suggested_titles)
    print(f"\nArtigo salvo em artigo_{topic.replace(' ', '_').lower()}.md")

if __name__ == "__main__":
    tema_exemplo = "Impacto da Inteligência Artificial no Mercado de Trabalho Brasileiro"
    tom_exemplo = "técnico"

    if len(sys.argv) > 2:
        tema_exemplo = sys.argv[1]
        tom_exemplo = sys.argv[2]
    elif len(sys.argv) == 2:
        print("Uso: python main.py \"Tema do Artigo\" \"Tom do Texto (informal, técnico, persuasivo)\"")
        sys.exit(1)
    
    run_blog_generator(tema_exemplo, tom_exemplo)