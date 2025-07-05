import agentops
from openai import OpenAI
from agentops.sdk.decorators import agent, operation
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize AgentOps
agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"), tags=["production"])

# Define an agent
@agent(name="assistant")
class AssistantAgent:
    def __init__(self):
        self.client = OpenAI()
    
    @operation
    def answer_question(self, question):
        # This LLM call will be automatically tracked and associated with this agent
        response = self.client.responses.create(
            model="gpt-4.1",
            instructions="Talk like a pirate.",
            input=question,
        )
        return response.output_text

def workflow():
    # Use the agent
    assistant = AssistantAgent()
    answer = assistant.answer_question("What's the capital of France?")
    print(answer)

workflow()
# Session is automatically tracked until application terminates