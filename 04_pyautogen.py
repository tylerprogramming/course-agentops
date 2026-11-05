from dotenv import load_dotenv
import os
import agentops
import autogen

# Load environment variables from .env file
load_dotenv()

# Initialize AgentOps
agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"))

# Configure your AG2 agents
config_list = [
    {
        # gpt-4.1 is removed from the API on 2027-01-14; gpt-6-luna is OpenAI's replacement.
        # autogen 0.14 has no built-in price for gpt-6-luna, so give it one
        # (USD per 1K input/output tokens) to keep the cost figures accurate.
        "model": "gpt-6-luna",
        "price": [0.0001, 0.0005],
        "api_key": os.getenv("OPENAI_API_KEY"),
    }
]

llm_config = {
    "config_list": config_list,
    "timeout": 60,
}

# Create a single agent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="You are a helpful AI assistant."
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"last_n_messages": 3, "work_dir": "coding"},
)

# Initiate a conversation
user_proxy.initiate_chat(
    assistant,
    message="Can you help me create a simple beginner course on python?"
)