from agency_swarm.agents import Agent


class DataCompiler(Agent):
    def __init__(self):
        super().__init__(
            name="DataCompiler",
            description="Responsible for organizing the data collected by the Research Analyst into structured lists and detailed overviews of each firm.",
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
