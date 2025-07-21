from crewai import Task

class BlogTasks:
    def research_task(self, agent, topic):
        return Task(
            description=f"Pesquisar e coletar informações chave e tendências sobre o tema '{topic}'. Focar em dados relevantes que possam ser usados para construir um artigo de blog informativo. O resultado deve ser um resumo conciso das informações coletadas, pronto para ser usado por outros agentes.",
            expected_output=f"Um resumo detalhado e conciso das informações essenciais sobre o tema '{topic}', incluindo dados importantes, pontos de vista relevantes e curiosidades.",
            agent=agent
        )

    def structure_task(self, agent, topic, context):
        return Task(
            description=f"Com base no resumo da pesquisa sobre '{topic}' (disponível no contexto da tarefa anterior) e nas melhores práticas de SEO e engajamento, crie uma estrutura detalhada para o artigo de blog. A estrutura deve incluir: uma introdução envolvente, 3 a 5 tópicos principais com subseções claras, e uma conclusão impactante. Para cada seção, inclua um breve descritivo do que deve ser abordado. O resultado deve ser a estrutura formatada.",
            expected_output=f"Uma estrutura completa e lógica para o artigo de blog sobre '{topic}', formatada claramente com títulos de seção e descrições para cada parte: Introdução, Tópicos Principais (com subseções se aplicável) e Conclusão.",
            agent=agent,
            context=[context]
        )

    def write_content_task(self, agent, topic, tone, context):
        return Task(
            description=f"Escrever o conteúdo completo do artigo de blog sobre '{topic}' com base na estrutura fornecida e nas informações detalhadas da pesquisa (ambos disponíveis no contexto). O tom do texto deve ser '{tone}'. Garanta que a linguagem seja envolvente, acessível e profissional, e que o artigo tenha um mínimo de 800 palavras. Crie um artigo coerente e bem desenvolvido, preenchendo cada seção da estrutura.",
            expected_output=f"O artigo de blog completo sobre '{topic}' com o tom '{tone}', seguindo a estrutura fornecida e com no mínimo 800 palavras, abordando todas as informações pesquisadas.",
            agent=agent,
            context=context
        )

    def suggest_titles_task(self, agent, topic, context):
        return Task(
            description=f"Com base no artigo completo sobre '{topic}' (disponível no contexto), gere pelo menos 3 títulos alternativos criativos e otimizados. Em seguida, formate a saída final. O resultado final deve conter o artigo completo primeiro, seguido por uma seção clara com os títulos sugeridos.",
            expected_output=f"A saída final formatada em markdown contendo o artigo de blog completo sobre '{topic}', seguido pela seção '--- Títulos Alternativos ---' e uma lista numerada de no mínimo 3 títulos de blog criativos.",
            agent=agent,
            context=[context]
        )