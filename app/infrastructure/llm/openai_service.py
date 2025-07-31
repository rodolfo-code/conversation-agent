import os
import logging
from langchain_core.messages import BaseMessage
from langchain_core.language_models import BaseLanguageModel
from langchain_openai import ChatOpenAI

logger = logging.getLogger(__name__)
from app.application.agent.conversation_agent.node_functions.gateway_node.mr_couch_service_prompt import MR_COUCH_SERVICES_TEMPLATE
from app.infrastructure.config.config import settings
from app.application.interfaces.illm_service import ILLMService

class OpenAIService(ILLMService):
    """Service for OpenAI language models."""
    def __init__(self):
        self.client = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=settings.OPENAI_MODEL_NAME,
            temperature=settings.OPENAI_TEMPERATURE
        )


    def conversation(self, messages: list[BaseMessage]) -> str:
        """Conversation with the OpenAI model."""

        chain = MR_COUCH_SERVICES_TEMPLATE | self.client

        logger.info("Conversation with the OpenAI model.", extra={"messages": messages})

        try:
            # Extrai a mensagem do usuário (assumindo que é a última mensagem)
            user_message = messages[-1].content if messages else ""

            services_1_content, services_2_content = self.load_service_info()

            # Invoca o LLM
            llm_response = chain.invoke({
                "input": user_message, 
                "services_1_content": services_1_content, 
                "services_2_content": services_2_content
            })
            
            return llm_response.content
        
        except Exception as e:
            logger.error("Error in conversation with the OpenAI model.", extra={"error": e})
            raise e
        

    def load_service_info(self):
        """Carrega as informações dos serviços dos arquivos .md"""
        # Caminho para os arquivos .md no diretório gateway_node
        current_dir = os.path.dirname(os.path.abspath(__file__))
        gateway_node_dir = os.path.join(
            current_dir, "..", "..",
            "application", "agent", "conversation_agent", "node_functions", "gateway_node"
        )
        
        services_1_path = os.path.join(gateway_node_dir, "services_1.md")
        services_2_path = os.path.join(gateway_node_dir, "services_2.md")
        
        services_1_content = ""
        services_2_content = ""
        
        try:
            with open(services_1_path, 'r', encoding='utf-8') as f:
                services_1_content = f.read()
        except FileNotFoundError:
            print(f"Arquivo {services_1_path} não encontrado")
        
        try:
            with open(services_2_path, 'r', encoding='utf-8') as f:
                services_2_content = f.read()
        except FileNotFoundError:
            print(f"Arquivo {services_2_path} não encontrado")
        
        return services_1_content, services_2_content
        
        