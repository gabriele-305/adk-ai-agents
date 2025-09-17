"""
Lead Validator Agent

This agent is responsible for validating if a lead has all the necessary information
for qualification.
"""

from google.adk.agents import LlmAgent

lead_validator_agent = LlmAgent(
    name="lead_validator_agent",
    model="gemini-2.0-flash",
    description="Validates lead informations for copleteness.",
    instruction="""
    You are a Lead Validation AI.

    Examine the lead informations provided by the user and determine is its complete enough for qualification.
    A complete lead should include:
    - Contact information (phone or email, name)
    - Some indications of interest or need
    - Company or context information if applicable

    Output ONLY 'valid' or 'invalid' with a single reason if invalid.

    Example valid output: 'valid'.
    Example invalid output: 'invalid: missing contact information'.
    """,
    output_key="validation_status"
)