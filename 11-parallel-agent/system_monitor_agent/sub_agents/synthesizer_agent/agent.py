"""
System Report Synthesizer Agent

This agent is responsible for synthesizing information from other agents
to create a comprehensive system health report.
"""
from google.adk.agents import LlmAgent

synthesizer_agent = LlmAgent(
    name="synthesizer_agent",
    model="gemini-2.0-flash",
    description="Synthesizes all system information into a comprehensive report",
    instruction="""
    You are a System Report Sinthesizer.

    You task is to create a comprehensive healt report by combining informations from:
    - CPU informations: {cpu_info}
    - Disk informations: {disk_info}
    - Memory informations: {memory_info}

    Create a well-formatted report with:
    1. An executive summary at the top with overall system healt status
    2. Sections for each component with their respective information
    3. Reccomendation based on every concerning metrics

    Use markdown formatting to make the report readable and professional.
    Highlight any concerning value and provide practical recommendations.
    """,
)