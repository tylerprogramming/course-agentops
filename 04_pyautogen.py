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
        "model": "gpt-4.1",
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