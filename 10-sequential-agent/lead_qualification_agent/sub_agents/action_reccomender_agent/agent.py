"""
Action Recommender Agent

This agent is responsible for recommending appropriate next actions
based on the lead validation and scoring results.
"""

from google.adk.agents import LlmAgent

action_reccomender_agent = LlmAgent(
    name="action_reccomender_agent",
    model="gemini-2.0-flash",
    description="Reccomends next action based on lead qualification.",
    instruction="""
    You are an Action Reccomendation AI.

    Based on the lead information and scoring:
    - For invalid leads: suggest what additional information is needed
    - For leads scored 1-3: suggest nortoring actions (educational content, etc.)
    - For leads scored 4-7: suggest qualifying actions (discovery calls, needs assesment)
    - For leads scored 8-10: suggest sales actions (demo, proposal, etc.)

    Format your response as a complete reccomendation to the sales team.

    Lead score:
    {lead_score}

    Lead validation status:
    {lead_validation_status}  
    """,
    output_key="action_reccomendation"
)