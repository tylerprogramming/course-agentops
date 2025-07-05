import agentops
from agentops.sdk.decorators import agent, operation, trace
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize AgentOps without auto-starting session since we use @trace
agentops.init(os.getenv("AGENTOPS_API_KEY"), auto_start_session=False)

# Create a decorated agent class
@agent(name='ResearchAgent')
class MyAgent:
    def __init__(self):
        self.client = OpenAI()
        
    @operation
    def search(self, query):
        response = self.client.responses.create(
            model="gpt-4.1",
            instructions="Talk like a pirate.",
            input=query,
        )
        return response.output_text

# Create a trace to group the agent operations
@trace(name="research-workflow")
def research_workflow(topic):
    agent = MyAgent()
    result = agent.search(topic)
    return result

# Execute the function to properly register the agent span
result = research_workflow("quantum computing")