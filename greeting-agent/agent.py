from google.adk.agents import Agent

root_agent = Agent(
    name="greeting-agent",
    description="greeting agent",
    model="gemini-2.5-flash",
    instruction="""You are a greeting agent. Greet the user.""",
    
)   