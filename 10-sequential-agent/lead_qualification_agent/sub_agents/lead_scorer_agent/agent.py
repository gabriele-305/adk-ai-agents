"""
Lead Validator Agent

This agent is responsible for validating if a lead has all the necessary information
for qualification.
"""

from google.adk.agents import LlmAgent

lead_scorer_agent = LlmAgent(
    name="lead_scorer_agent",
    model="gemini-2.0-flash",
    description="Scores qualified leads on a scale of 1-10.",
    instruction="""
    You are a Lead Scoring AI.

    Analyze the lead informations and assign a qualification score from 1-10 based on:
    - Expressed need (urgency/clarity of the problem)
    - Decision making authority
    - Budget indicators
    - Timeline indicators

    Output ONLY a numerica score and ONE sentence justification.

    Example output: '8: Decision maker with clear budget and immediate need'
    Example output: '3: Vague interest with no timeline or budget mentioned'
    """,
    output_key="lead_score"
)