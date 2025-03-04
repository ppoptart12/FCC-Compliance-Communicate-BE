from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid


class ComplianceDataItem(BaseModel):
    """Schema for a single compliance data item."""
    content: str
    source: Optional[str] = None


class ComplianceScanRequest(BaseModel):
    """Schema for compliance scan request."""
    compliance_data: List[ComplianceDataItem]
    questions: List[str]
    user_context: Optional[Dict[str, Any]] = None  # Raw JSON context from frontend


class DetailedComplianceReport(BaseModel):
    """Schema for detailed compliance report."""
    compliance_score: int = Field(..., description="Numerical score (0-100)")
    compliance_status: str = Field(..., description="Detailed compliance status")
    summary_of_findings: str = Field(..., description="Overall summary text")
    section_breakdown: str = Field(..., description="Text describing compliance by section")
    specific_issues: str = Field(..., description="Text listing specific compliance issues found")
    recommendations: str = Field(..., description="Text with recommendations to address issues")
    section_scores: Dict[str, int] = Field(..., description="Object mapping section names to numerical scores")


class ScannedDocument(BaseModel):
    """Schema for scanned document."""
    id: str = Field(default_factory=lambda: f"doc_{uuid.uuid4().hex[:8]}")
    name: str
    size: str
    uploadTime: str = Field(default_factory=lambda: datetime.now().isoformat())
    progress: int = 100
    status: str = "complete"
    complianceStatus: str
    complianceMessage: str
    detailedReport: DetailedComplianceReport


class ComplianceScanResponse(BaseModel):
    """Schema for compliance scan response."""
    document: ScannedDocument
    message: str = "Document scan completed successfully"


class OrganizationContext(BaseModel):
    """Schema for organization context in file upload requests."""
    name: str
    industry: Optional[str] = None
    products_services: Optional[List[str]] = None
    size: Optional[str] = None
    additional_info: Optional[Dict[str, Any]] = None
