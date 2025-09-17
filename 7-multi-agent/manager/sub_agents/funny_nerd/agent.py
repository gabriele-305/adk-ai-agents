from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext

def get_nerd_joke(topic: str, tool_context: ToolContext)-> dict:
    """Get a nerdy jokes about a specific topic."""
    print(f"--- Tool: get_nerd_joke called for topic: {topic} ---")

    # Example jokes - in a real implementation, you might want to use an API
    jokes = {
        "python": "Why don't Python programmers like to use inheritance? Because they don't like to inherit anything!",
        "javascript": "Why did the JavaScript developer go broke? Because he used up all his cache!",
        "java": "Why do Java developers wear glasses? Because they can't C#!",
        "programming": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "math": "Why was the equal sign so humble? Because he knew he wasn't less than or greater than anyone else!",
        "physics": "Why did the photon check a hotel? Because it was travelling light!",
        "chemistry": "Why did the acid go to the gym? To become a buffer solution!",
        "biology": "Why did the cell go to therapy? Because it had too many issues!",
        "default": "Why did the computer go to the doctor? Because it had a virus!",
    }

    joke = jokes.get(topic.lower(), jokes["default"])
    tool_context.state["last_joke_topic"] = topic

    return {"status": "success", "joke": joke, "topic": topic}

funny_nerd = Agent(
    name="funny_nerd",
    model="gemini-2.0-flash",
    description="An agent the tells nerdy jokes about various topic",
    instruction="""
    You are a funny nerd agent that tells funny nerdy jokes about various topics.

    When asked to tell joke:
    1. Use the get_nerd_joke to fetch a joke about the request topic.
    2. If no specific topic is mentioned, tell the user all the possible topics and ask the user what kind of nerdy jokes they'd like to hear.
    3. Format the response to include both the joke and a brief explanation if needed.

    Available topics include:
    - python
    - java
    - javascript
    - programming
    - math
    - physics
    - cheminstry
    - biology

    Example response format:
    "Here's a nerdy jokes about <TOPIC>:
    <JOKE>

    Explanation: {brief explanation if needed}"

    If the user asks about anything else besides jokes,
    you should delegate the task to the root agent.
    """,
    tools=[get_nerd_joke]
)