from agency_swarm.agents import Agent


class ResearchAnalyst(Agent):
    def __init__(self):
        super().__init__(
            name="ResearchAnalyst",
            description="Responsible for searching and gathering data on private equity firms that specialize in healthcare investments.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
