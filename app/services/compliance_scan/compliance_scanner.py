from langchain_openai import ChatOpenAI
from app.core import config
from app.services.compliance_scan.llm_models import (ComplianceScanAgentPrompts, compliance_scan as ComplianceScanSchema)


class ComplianceScanAgent():
    def __init__(self):
        self.open_ai_key = config.get("OPENAI_KEY")
        self.llm_model = config.get("OPENAI_LLM_MODEL")
        self.llm_model_temperature = config.get("AGENT_TEMPERATURE")

    def generate_compliance_scan(self, compliance_data):
        llm = ChatOpenAI(api_key=str(self.open_ai_key), model=str(self.llm_model))  # experiment with temperature and top-p
        prompt = ComplianceScanAgentPrompts.compliance_scan_agent
        compliance_scan_agent = prompt | llm.with_structured_output(schema=ComplianceScanSchema)

        result = compliance_scan_agent.invoke({
            "compliance_data": compliance_data["compliance_data"],
            "questions": compliance_data["questions"],
        })
        return result