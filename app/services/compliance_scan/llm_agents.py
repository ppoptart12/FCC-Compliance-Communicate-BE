from langchain_openai import ChatOpenAI
from app.core import config
from app.services.lab_reports.llm_models import (LabAgentPrompts, lab_in_range, lab_out_of_range, lab_classification_model, patient_insights_model)
from app.core.logging_config import logger


class LabInRangeAgent():
    def __init__(self):
        self.open_ai_key = config.get("OPENAI_KEY")
        self.llm_model = config.get("OPENAI_LLM_MODEL")
        self.llm_model_temperature = config.get("AGENT_TEMPERATURE")

    def generate_in_range_patient_note(self, lab_data):
        llm = ChatOpenAI(api_key=str(self.open_ai_key), model=str(self.llm_model))  # experiment with temperature and top-p
        prompt = LabAgentPrompts.lab_in_range_prompt
        lab_in_range_agent = prompt | llm.with_structured_output(schema=lab_in_range)

        in_range_patient_note = lab_in_range_agent.invoke({
            "current_lab_results": lab_data["current_lab_results"],
            "past_lab_data": "",  #lab_data["past_lab_results"],
            "active_problems": lab_data["active_problems"],
            "patient_age": lab_data["patient_age"],
            "patient_gender": lab_data["patient_gender"],
            "medications": lab_data["medications"],
            "patient_height_weight": lab_data["vitals"],
            "vaccines": lab_data["vaccines"],
            "instructions": lab_data["user_preferences"]
        })
        return in_range_patient_note


class LabOutOfRangeAgent():  # Add past patient data/labs, charts, etc
    def __init__(self):
        self.open_ai_key = config.get("OPENAI_KEY")
        self.llm_model = config.get("OPENAI_LLM_MODEL")
        self.llm_model_temperature = config.get("AGENT_TEMPERATURE")

    def generate_out_of_range_patient_note(self, lab_data):
        llm = ChatOpenAI(api_key=str(self.open_ai_key), model=str(self.llm_model))  # experiment with temperature and top-p
        prompt = LabAgentPrompts.lab_out_of_range_prompt
        lab_out_of_range_agent = prompt | llm.with_structured_output(schema=lab_out_of_range)

        out_of_range_patient_note = lab_out_of_range_agent.invoke({
            "current_lab_results": lab_data["current_lab_results"],
            "past_lab_data": "", #lab_data["past_lab_results"],
            "active_problems": lab_data["active_problems"],
            "patient_age": lab_data["patient_age"],
            "patient_gender": lab_data["patient_gender"],
            "medications": lab_data["medications"],
            "patient_height_weight": lab_data["vitals"],
            "vaccines": lab_data["vaccines"],
            "instructions": lab_data["user_preferences"]
        })
        return out_of_range_patient_note


class LabClassifierAgent():
    # This agent determines if a lab is clinically relevant or irrelevant
    def __init__(self):
        self.open_ai_key = config.get("OPENAI_KEY")
        self.llm_model = config.get("OPENAI_LLM_MODEL")
        #self.llm_model_temperature = config.get("AGENT_TEMPERATURE")

    def is_lab_clinically_relevant(self, patient_data, past_lab_data, lab_data):
        llm = ChatOpenAI(api_key=str(self.open_ai_key), model=str(self.llm_model))  # experiment with temperature and top-p
        prompt = LabAgentPrompts.lab_classifier_agent
        lab_classifier_agent = prompt | llm.with_structured_output(schema=lab_classification_model)

        lab_classification = lab_classifier_agent.invoke({"patient_data": patient_data, "past_lab_data": past_lab_data, "lab_data": lab_data})
        return lab_classification


class PatientInsightsAgent():
    def __init__(self):
        self.open_ai_key = config.get("OPENAI_KEY")
        self.llm_model = config.get("OPENAI_LLM_MODEL")
        #self.llm_model_temperature = config.get("AGENT_TEMPERATURE")

    def generate_patient_insights(self, lab_data):
        llm = ChatOpenAI(api_key=str(self.open_ai_key), model=str(self.llm_model))  # experiment with temperature and top-p
        prompt = LabAgentPrompts.patient_insights_prompt
        patient_insights_agent = prompt | llm.with_structured_output(schema=patient_insights_model)

        patient_insights_note = patient_insights_agent.invoke({
            "current_lab_results": lab_data["current_lab_results"],
            "past_lab_data": "", #lab_data["past_lab_results"],
            "active_problems": lab_data["active_problems"],
            "patient_age": lab_data["patient_age"],
            "patient_gender": lab_data["patient_gender"],
            "medications": lab_data["medications"],
            "patient_height_weight": lab_data["vitals"],
            "vaccines": lab_data["vaccines"],
            #"instructions": lab_data["user_preferences"]
        })
        return patient_insights_note
    