"""
System Monitor Root Agent

This module defines the root agent for the system monitoring application.
It uses a parallel agent for system information gathering and a sequential
pipeline for the overall flow.
"""

from google.adk.agents import ParallelAgent, SequentialAgent
from .sub_agents.cpu_info_agent.agent import cpu_info_agent
from .sub_agents.disk_info_agent.agent import disk_info_agent
from .sub_agents.memory_info_agent.agent import memory_info_agent
from .sub_agents.synthesizer_agent.agent import synthesizer_agent

system_info_gatherer = ParallelAgent(
    name="system_info_gatherer",
    sub_agents=[cpu_info_agent, disk_info_agent, memory_info_agent]
)

root_agent = SequentialAgent(
    name="system_monitor_agent",
    sub_agents=[system_info_gatherer, synthesizer_agent]
)