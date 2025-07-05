import agentops
from agentops.sdk.decorators import agent, operation, tool, trace
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize AgentOps without auto-starting session since we use @trace
agentops.init(os.getenv("AGENTOPS_API_KEY"), auto_start_session=False)

@agent
class DataCollectionAgent:
    @tool(cost=0.02)
    def fetch_data(self, source):
        return f"Data from {source}"

@agent  
class AnalysisAgent:
    @operation
    def analyze_data(self, data):
        return f"Analysis of {data}"

@agent
class ReportingAgent:
    @tool(cost=0.01)
    def generate_report(self, analysis):
        return f"Report: {analysis}"

@trace(name="multi-agent-workflow")
def collaborative_workflow(data_source):
    """Workflow using multiple specialized agents"""
    
    # Data collection
    collector = DataCollectionAgent()
    raw_data = collector.fetch_data(data_source)
    
    # Analysis
    analyzer = AnalysisAgent()
    analysis = analyzer.analyze_data(raw_data)
    
    # Reporting
    reporter = ReportingAgent()
    report = reporter.generate_report(analysis)
    
    return {
        "source": data_source,
        "analysis": analysis,
        "report": report
    }

# Run the collaborative workflow
result = collaborative_workflow("customer_database")