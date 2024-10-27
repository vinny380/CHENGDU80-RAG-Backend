from agents.imports import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT
from langchain_openai import AzureChatOpenAI


LLM_CHAT = AzureChatOpenAI(
    azure_deployment="gpt-4", 
    api_version="2024-02-01",
    temperature=0.4,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def complete(prompt: str) -> dict:
    """Does what the user says!"""
    messages = [
        (
        "system",
        """As an insurance specialist for autonomous vehicles (AV), your task is to draft tailored insurance policies based on a user's profile and their specific AV model. Consider that the AV can operate independently without the user's direct control, which may lead to autonomous accidents. Your objective is to create the most advantageous insurance policy that maximizes revenue and minimizes risks for the insurance company, while also ensuring it is competitive and appealing enough to retain the customer over other providers.

            Please format your response in JSON, including distinct sections with titles and detailed content. Each section should address different aspects of the policy. Here is the structure to follow:

            {
            "title": "Customized AV Insurance Policy",
            "sections": [
                {
                "section_title": "Coverage and Clauses",
                "section_content": "Details the specific coverage items and clauses relevant to autonomous operation and user control scenarios."
                },
                {
                "section_title": "Liability and Responsibilities",
                "section_content": "Outlines the division of financial responsibility between the insurance holder and the company in cases of autonomous accidents."
                },
                {
                "section_title": "Pricing and Payment",
                "section_content": "Provides a breakdown of premium calculations, discounts, and payment schedules."
                }
            ],
            "metadata" : {
                "price" : 100, -- how much the user will pay per month
                "AI_safety_score" : 90 -- how safe the autodrive of their car is.
                "driver_behaviour" : -- description of the driver behaviour given the user's data.,
                "deductible" : -- how much the customer will pay out of pocket
                

            }
            }
        """,
        ),
        ("human", prompt),
    ]
    ai_msg = LLM_CHAT.invoke(messages)
    return ai_msg


def prompt_optimization(prompt: str) -> dict:
    messages = [
        (
            "system",
            """You're a specialist in prompt engineering for LLMs. Optimize the user prompt
            for optimal results with LLMs.
            """,
        ),
        ("human", prompt),
    ]
    ai_msg = LLM_CHAT.invoke(messages)
    return ai_msg

if __name__ == '__main__':
    result = prompt_optimization("")