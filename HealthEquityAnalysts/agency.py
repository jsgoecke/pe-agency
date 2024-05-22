from agency_swarm import Agency
from DataCompiler import DataCompiler
from ResearchAnalyst import ResearchAnalyst
from HealthEquityCEO import HealthEquityCEO

healthEquityCEO = HealthEquityCEO()
researchAnalyst = ResearchAnalyst()
dataCompiler = DataCompiler()

agency = Agency([healthEquityCEO, researchAnalyst, [healthEquityCEO, researchAnalyst],
                 [healthEquityCEO, dataCompiler],
                 [researchAnalyst, dataCompiler]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()