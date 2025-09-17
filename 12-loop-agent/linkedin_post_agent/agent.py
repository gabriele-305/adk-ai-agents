"""
LinkedIn Post Generator Root Agent

This module defines the root agent for the LinkedIn post generation application.
It uses a sequential agent with an initial post generator followed by a refinement loop.
"""
from google.adk.agents import LoopAgent, SequentialAgent
from .sub_agents.post_generator.agent import initial_post_generator
from .sub_agents.post_refiner.agent import post_refiner
from .sub_agents.post_reviewer.agent import post_reviewer

refinement_loop = LoopAgent(
    name="refinement_loop",
    max_iterations=10,
    sub_agents=[post_reviewer, post_refiner],
    description="Iteratively review and refine a linkedin post until quality requirement are met."
)

root_agent = SequentialAgent(
    name="linkedin_post_agent",
    sub_agents=[initial_post_generator, refinement_loop],
    description="Generates and refine a linkedin post through an iterative review process."
)