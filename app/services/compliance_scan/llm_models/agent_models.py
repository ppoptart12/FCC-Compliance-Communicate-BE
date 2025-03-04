from pydantic import BaseModel, Field
from typing import Dict


class SectionScores(BaseModel):
    """Model for section scores in compliance report."""
    # Using the exact section names from the frontend
    public_file_requirements: int = Field(..., description="Score for Public File Requirements (0-100)")
    technical_compliance: int = Field(..., description="Score for Technical Compliance (0-100)")
    ownership_disclosure: int = Field(..., description="Score for Ownership Disclosure (0-100)")
    eas_compliance: int = Field(..., description="Score for EAS Compliance (0-100)")
    rf_exposure: int = Field(..., description="Score for RF Exposure (0-100)")


class DetailedReport(BaseModel):
    """Model for detailed compliance report."""
    compliance_score: int = Field(..., description="Overall compliance score (0-100)")
    compliance_status: str = Field(..., description="Detailed compliance status (e.g., 'Partial Compliance')")
    summary_of_findings: str = Field(..., description="Summary of the compliance findings")
    section_breakdown: str = Field(..., description="Breakdown of compliance by section")
    specific_issues: str = Field(..., description="List of specific compliance issues found")
    recommendations: str = Field(..., description="Recommendations to address compliance issues")
    section_scores: Dict[str, int] = Field(..., description="Scores for each compliance section")


class compliance_scan(BaseModel):
    """Model for compliance scan response."""
    compliance_score: int = Field(..., description="Overall compliance score (0-100)")
    compliance_status: str = Field(..., description="Overall compliance status ('compliant', 'issues', or 'review')")
    compliance_message: str = Field(..., description="Human-readable message explaining the compliance status")
    detailed_report: DetailedReport = Field(..., description="Detailed compliance report")