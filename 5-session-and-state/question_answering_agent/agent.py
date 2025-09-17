from google.adk.agents import Agent

question_answering_agent = Agent(
    name="question_answering_agent",
    model="gemini-2.0-flash",
    description="Question answering agent",
    instruction="""
    You are a helpful assistant that answer questions about the user's preferences.

    Here is some usefull information about the user:
    Name: 
    {user_name}
    Preferences:
    {user_preferences}
    """
)