from langchain_core.prompts import ChatPromptTemplate


class ComplianceScanAgentPrompts:
    compliance_scan_agent = ChatPromptTemplate.from_messages(
            [
                (
                    "You are an FCC compliance expert. You will be given a compliance document and a list of questions."
                ),
                (
                    "user",
                    "<Compliance Data>"
                    "{compliance_data}"
                    "<Compliance Data>"
                    ),
            ]
        )
