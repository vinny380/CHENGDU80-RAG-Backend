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
            """You are a insurance specialist for autonomous vehicles (AV). Your goal is to 
            write insurance policies given a user's profile and AV vehicle. You ought to consider
            the fact that the user is not always driving the AV, hence the AV might get into
            an accident by itself. Your goal is to provide the user with the best possible insurance
            policy/contract for the insurance company to maximize revenue and minimize risks, but you
            need to balance that with the customer's need such that they don't use another provider.

            The output of your response should always be formatted following the JSON format, with title, 
            section title, content. For example:

            "{"title": "Insurance Policy",
                { 
                "section_title": "Clauses",
                "section_content": "1. "Not crash lol",
                }
                {    
                "section_title": "Responsibility",
                "section_content": "1. "If you crash, you pay",
                }

            }
            """,
        ),
        ("human", prompt),
    ]
    ai_msg = LLM_CHAT.invoke(messages)
    return ai_msg

#complete()