from langchain_core.prompts import ChatPromptTemplate


class ComplianceScanAgentPrompts:
    compliance_scan_agent = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an FCC compliance expert. You will be given a compliance document and a list of questions. "
                    "Analyze the document and answer the questions based on FCC regulations and compliance requirements."
                ),
                (
                    "user",
                    "Compliance Data:\n{compliance_data}\n\n"
                    "Questions:\n{questions}"
                ),
            ]
        )
