from pydantic import BaseModel
from typing import List, Optional


class ComplianceDataItem(BaseModel):
    """Schema for a single compliance data item."""
    content: str
    source: Optional[str] = None


class ComplianceScanRequest(BaseModel):
    """Schema for compliance scan request."""
    compliance_data: List[ComplianceDataItem]
    questions: List[str]


class ComplianceScanResponse(BaseModel):
    """Schema for compliance scan response."""
    compliance_scan: str 