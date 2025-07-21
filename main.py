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
    reviser = agents.reviser_formatter_agent()

    research_task = tasks.research_task(researcher, topic)
    structure_task = tasks.structure_task(
        agent=structurer,
        topic=topic,
        context=[research_task]
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
        context=[write_content_task]
    )
    revise_and_format_task = tasks.revise_and_format_task(
        agent=reviser,
        topic=topic,
        context=[suggest_titles_task]
    )

    blog_crew = Crew(
        agents=[researcher, structurer, writer, title_suggester, reviser],
        tasks=[research_task, structure_task, write_content_task, suggest_titles_task, revise_and_format_task],
        verbose=True,
        process=Process.sequential
    )

    final_result = blog_crew.kickoff()

    if final_result and final_result.raw and final_result.raw.strip():
        return final_result.raw
    else:
        return "Ocorreu um erro ou o resultado final está vazio. Nenhum conteúdo foi gerado."

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Artigos para Blog (Versão Linha de Comando)!")
    if len(sys.argv) == 3:
        tema_digitado = sys.argv[1]
        tom_digitado = sys.argv[2]
    else:
        tema_digitado = input("Digite o tema do artigo: ")
        while True:
            tom_digitado = input("Digite o tom do texto (Informal, Técnico, Persuasivo, Informativo, Instrutivo/Didático, Irônico/Sarcástico, Crítico): ").lower()
            if tom_digitado in ["Informal", "Técnico", "Persuasivo", "Informativo", "Instrutivo/Didático", "Irônico/Sarcástico", "Crítico"]:
                break
            else:
                print("Tom inválido. Por favor, escolha entre 'Informal', 'Técnico', 'Persuasivo', 'Informativo', 'Instrutivo/Didático', 'Irônico/Sarcástico' ou 'Crítico'.")

    print("\n#### Iniciando o processo de geração do artigo... ####")
    resultado_final = run_blog_generator(tema_digitado, tom_digitado)
    print("\n#### Processo Concluído! ####\n")

    print("\n--- Resultado Gerado ---")
    print(resultado_final)

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    file_name = f"artigo_{tema_digitado.replace(' ', '_').lower()}.md"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(resultado_final)
    
    print(f"\nArtigo salvo em {file_path}")