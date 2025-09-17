"""
LinkedIn Post Generator Agent

This agent generates the initial LinkedIn post before refinement.
"""
from google.adk.agents import LlmAgent

initial_post_generator = LlmAgent(
    name="post_generator",
    model="gemini-2.0-flash",
    description="Generates the initial linkedin post to start the refinement process",
    instruction="""
    You are a Linkedin Post Generator.

    Your task is to create a linkedin post about an Agent Development Kit (ADK) tutorial.

    ## CONTENT REQUIREMENTS
    Ensure the post includes:
    1. Excitement about learning from the tutorial
    2. Specific aspect of ADK learned and skill improvements:
        - Basic agent implementation (basic-agent)
        - Tool integration (tool-agent)
        - Using LiteLLM (litellm-agent)
        - Managing sessions and memory
        - Persistent storage capabilities
        - Multi-agent orchestration
        - Stateful multi-agent systems
        - Callback systems
        - Sequential agents for pipeline workflows
        - Parallel agents for concurrent operations
        - Loop agents for iterative refinement
    3. Brief statement about improving AI applications
    4. New skill learned for the job-world application
    5. Clear call-to-action for connections

    ## STYLE REQUIREMENTS
    - professional and conversational tone
    - Between 1000-1500 characters
    - NO emojis
    - NO hashtags
    - Show genuine enthusiasm
    - Highlight practical application

    ## UOTPUT INSTRUCTIONS
    - Return ONLY the post content
    - Do not add formatting markes or explanations 
    """,
    output_key="current_post"
)