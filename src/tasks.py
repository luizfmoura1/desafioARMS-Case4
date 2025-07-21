from crewai import Task

class BlogTasks:
    def research_task(self, agent, topic):
        return Task(
            description=f"Pesquisar e coletar informações chave e tendências sobre o tema '{topic}'. Focar em dados relevantes que possam ser usados para construir um artigo de blog informativo. O resultado deve ser um resumo conciso das informações coletadas.",
            expected_output=f"Um resumo detalhado das informações essenciais sobre o tema '{topic}', incluindo dados importantes, pontos de vista relevantes e curiosidades.",
            agent=agent
        )

    def structure_task(self, agent, research_summary, topic):
        return Task(
            description=f"Com base no resumo da pesquisa sobre '{topic}' e nas melhores práticas de SEO e engajamento, crie uma estrutura detalhada para o artigo de blog. A estrutura deve incluir: uma introdução envolvente, 3 a 5 tópicos principais com subseções claras, e uma conclusão impactante. Para cada seção, inclua um breve descritivo do que deve ser abordado.",
            expected_output=f"Uma estrutura completa e lógica para o artigo de blog sobre '{topic}', formatada claramente com títulos de seção e descrições.",
            agent=agent
        )

    def write_content_task(self, agent, structure, research_summary, topic, tone):
        return Task(
            description=f"Escrever o conteúdo completo do artigo de blog sobre '{topic}' com base na estrutura fornecida e nas informações do resumo da pesquisa. O tom do texto deve ser '{tone}'. Garanta que a linguagem seja envolvente e acessível. O artigo deve ter um mínimo de 800 palavras.",
            expected_output=f"O artigo de blog completo sobre '{topic}' com o tom '{tone}', seguindo a estrutura fornecida e com no mínimo 800 palavras.",
            agent=agent
        )

    def suggest_titles_task(self, agent, article_content, topic):
        return Task(
            description=f"Gerar pelo menos 3 títulos alternativos criativos e otimizados para o artigo de blog sobre '{topic}'. Os títulos devem ser cativantes e relevantes para o conteúdo do artigo.",
            expected_output=f"Uma lista de no mínimo 3 títulos de blog criativos e impactantes para o artigo sobre '{topic}'.",
            agent=agent
        )