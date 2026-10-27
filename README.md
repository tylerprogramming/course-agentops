# AgentOps Course Repository

This repository contains a comprehensive course on **AgentOps** - an AI agent observability platform that helps you monitor, debug, and optimize your AI agents. The course includes practical examples and a complete CrewAI project demonstration.

## 📚 What You'll Learn

- How to integrate AgentOps for agent monitoring and observability
- Using decorators to track agent operations and workflows
- Multi-agent collaboration patterns
- Integration with popular AI frameworks like OpenAI and AutoGen
- Building complex agent workflows with CrewAI

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher (< 3.13 for CrewAI project)
- OpenAI API key
- AgentOps API key

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd course-agentops
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys:
   # AGENTOPS_API_KEY=your_agentops_api_key
   # OPENAI_API_KEY=your_openai_api_key
   ```

## 📁 Repository Structure

```
course-agentops/
├── 01_example.py          # Basic AgentOps integration
├── 02_multi-agent.py      # Multi-agent collaboration
├── 03_altogether.py       # Complete workflow example
├── 04_pyautogen.py        # AutoGen integration
└── story_flow/            # CrewAI project
    ├── src/story_flow/
    │   ├── crews/
    │   │   └── poem_crew/
    │   ├── tools/
    │   └── main.py
    └── pyproject.toml
```

## 📖 Course Examples

### 1. Basic AgentOps Integration (`01_example.py`)

Demonstrates the fundamental concepts:
- `@agent` decorator for agent definition
- `@operation` decorator for tracking operations
- `@trace` decorator for workflow grouping
- Manual session management

**Key Features:**
- Agent class with OpenAI integration
- Operation tracking
- Workflow tracing

### 2. Multi-Agent Collaboration (`02_multi-agent.py`)

Shows how multiple agents work together:
- Data collection agent
- Analysis agent
- Reporting agent
- Cost tracking with `@tool` decorator

**Key Features:**
- Multiple specialized agents
- Tool cost tracking
- Collaborative workflows

### 3. Complete Workflow (`03_altogether.py`)

Demonstrates production-ready patterns:
- Automatic session management
- Agent tagging
- Simplified workflow implementation

**Key Features:**
- Production tags
- Automatic session tracking
- Clean agent implementation

### 4. AutoGen Integration (`04_pyautogen.py`)

Shows AgentOps integration with Microsoft AutoGen:
- UserProxy and AssistantAgent setup
- Conversation initiation
- Code execution capabilities

**Key Features:**
- AutoGen framework integration
- Conversation management
- Code execution environment

This file uses the classic `import autogen` API, which `requirements.txt` installs as the `autogen` package (0.14.x, AG2 classic). Don't `pip install pyautogen`: that name is now an empty proxy for AutoGen 0.7 (`autogen-agentchat`), which has no `autogen` module, so the import fails.

The user proxy runs the code the assistant writes in Docker by default, so start Docker first. To run the code directly on your machine instead, set `AUTOGEN_USE_DOCKER=False` in your `.env`.

## 🎭 CrewAI Project (story_flow)

The `story_flow` directory contains a complete CrewAI project that generates poems using AgentOps monitoring.

### Features

- **Flow-based Architecture**: Uses CrewAI's Flow system for complex workflows
- **Agent Monitoring**: Full AgentOps integration for observability
- **Configuration-driven**: YAML-based agent and task configuration
- **Dynamic Content**: Generates poems with random sentence counts

### Running the CrewAI Project

1. Navigate to the story_flow directory:
   ```bash
   cd story_flow
   ```

2. Install dependencies:
   ```bash
   pip install uv
   uv sync
   ```

3. Run the project:
   ```bash
   crewai run
   ```

4. The generated poem will be saved to `poem.txt`

### CrewAI Project Structure

- **`main.py`**: Flow orchestration and AgentOps integration
- **`crews/poem_crew/`**: Poem generation crew implementation
- **`config/agents.yaml`**: Agent definitions and configurations
- **`config/tasks.yaml`**: Task descriptions and requirements
- **`tools/custom_tool.py`**: Custom tool implementations

## 🔧 Key AgentOps Features Demonstrated

### Decorators

- `@agent`: Marks classes as agents for tracking
- `@operation`: Tracks individual operations within agents
- `@tool`: Tracks tool usage and costs
- `@trace`: Groups related operations into workflows
- `@task`: Marks methods as tasks in workflows

### Session Management

- **Manual**: Using `auto_start_session=False` for custom control
- **Automatic**: Default behavior tracks entire application lifecycle

### Integration Patterns

- **OpenAI**: Direct API integration with automatic tracking
- **AutoGen**: Framework-level integration
- **CrewAI**: Flow-based multi-agent systems

## 📊 AgentOps Dashboard

Once you run the examples, you can view detailed analytics in your AgentOps dashboard:

- Agent performance metrics
- Operation costs and timing
- Workflow visualizations
- Error tracking and debugging

## 🛠️ Development

### Adding New Examples

1. Create a new Python file following the naming convention
2. Import AgentOps and necessary dependencies
3. Use appropriate decorators for tracking
4. Include proper error handling and logging

### Extending the CrewAI Project

1. Modify `config/agents.yaml` to add new agents
2. Update `config/tasks.yaml` for new tasks
3. Implement custom tools in `tools/custom_tool.py`
4. Update the flow logic in `main.py`

## 📚 Additional Resources

- [AgentOps Documentation](https://docs.agentops.ai/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [AutoGen Documentation](https://microsoft.github.io/autogen/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your examples or improvements
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter issues:

1. Check the AgentOps documentation
2. Verify your API keys are correctly set
3. Ensure all dependencies are installed
4. Check the example outputs for expected behavior

---

**Happy Learning!** 🎉

Start with `01_example.py` and work your way through the examples to master AgentOps integration patterns. 