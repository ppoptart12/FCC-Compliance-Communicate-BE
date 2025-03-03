from pydantic import BaseModel, Field


class compliance_scan(BaseModel):
    compliance_scan: str = Field(description="The compliance scan")
