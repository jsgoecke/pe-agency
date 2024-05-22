from agency_swarm.agents import Agent


class HealthEquityCEO(Agent):
    def __init__(self):
        super().__init__(
            name="HealthEquityCEO",
            description="Serves as the main point of contact for the user, managing requests and coordinating the activities of other agents within the HealthEquityAnalysts agency.",
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
