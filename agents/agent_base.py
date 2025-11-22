# agents/agent_base.py
import uuid
import logging

class AgentBase:
    def __init__(self, name, llm, memory, tools=None):
        self.name = name
        self.llm = llm
        self.memory = memory
        self.tools = tools if tools else []

    def log(self, msg):
        trace = uuid.uuid4().hex
        print(f"[{self.name}][{trace}] {msg}")

    async def run(self, context):
        raise NotImplementedError("Each agent must implement its own run method")
