from crewai import Crew, Process
from src.agents import BlogAgents
from src.tasks import BlogTasks
import sys
import os

def run_blog_generator(topic: str, tone: str):
    agents = BlogAgents()
    tasks = BlogTasks()

    researcher = agents.researcher_agent()
    structurer = agents.article_structurer_agent()
    writer = agents.content_writer_agent()
    title_suggester = agents.title_suggester_agent()

    research_task = tasks.research_task(researcher, topic)

    structure_task = tasks.structure_task(
        agent=structurer,
        topic=topic,
        context=research_task
    )

    write_content_task = tasks.write_content_task(
        agent=writer,
        topic=topic,
        tone=tone,
        context=[research_task, structure_task]
    )

    suggest_titles_task = tasks.suggest_titles_task(
        agent=title_suggester,
        topic=topic,
        context=write_content_task
    )

    blog_crew = Crew(
        agents=[researcher, structurer, writer, title_suggester],
        tasks=[research_task, structure_task, write_content_task, suggest_titles_task],
        verbose=True,
        process=Process.sequential
    )

    print("#### Iniciando o processo de geração do artigo... ####")
    final_result = blog_crew.kickoff()
    print("\n#### Processo Concluído! ####\n")

    print("\n--- Resultado Gerado ---")
    print(final_result)
    
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    file_name = f"artigo_{topic.replace(' ', '_').lower()}.md"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_result)
    
    print(f"\nArtigo salvo em {file_path}")

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Artigos para Blog!")
    if len(sys.argv) == 3:
        tema_digitado = sys.argv[1]
        tom_digitado = sys.argv[2]
    else:
        tema_digitado = input("Digite o tema do artigo: ")
        while True:
            tom_digitado = input("Digite o tom do texto (informal, técnico, persuasivo): ").lower()
            if tom_digitado in ["informal", "técnico", "persuasivo"]:
                break
            else:
                print("Tom inválido. Por favor, escolha entre 'informal', 'técnico' ou 'persuasivo'.")
    
    run_blog_generator(tema_digitado, tom_digitado)