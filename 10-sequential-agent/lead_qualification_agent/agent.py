"""
Sequential Agent with a Minimal Callback

This example demonstrates a lead qualification pipeline with a minimal
before_agent_callback that only initializes state once at the beginning.
"""

from google.adk.agents import SequentialAgent
from .sub_agents.action_reccomender_agent.agent import action_reccomender_agent
from .sub_agents.lead_scorer_agent.agent import lead_scorer_agent
from .sub_agents.lead_validator_agent.agent import lead_validator_agent

root_agent = SequentialAgent(
    name="lead_qualification_agent",
    sub_agents=[lead_validator_agent, lead_scorer_agent, action_reccomender_agent],
    description="A pipeline that validates, scores and reccomends actions for sales leads."
)