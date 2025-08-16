from langchain_core.prompts import ChatPromptTemplate

DECISION_NEXT_NODE_TEMPLATE = ChatPromptTemplate.from_template(
    """
    Você é um assistente virtual especialista em identificar a intenção do cliente e decidir qual o próximo nó a ser executado.

    Você deve responder com um dos seguintes valores:
    - "SERVICES_NODE"
    - "HOW_IT_WORKS_NODE"
    - "UNDEFINED"

    Pergunta do cliente: {input}
    """
)



