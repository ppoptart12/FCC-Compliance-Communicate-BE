from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.compliance_scan import ComplianceScanRequest, ComplianceScanResponse
from app.services.compliance_scan.compliance_scanner import ComplianceScanAgent

router = APIRouter()


@router.post("/compliance_scan", response_model=ComplianceScanResponse)
def run_compliance_scan(
    *,
    db: Session = Depends(get_db),
    compliance_data: ComplianceScanRequest
) -> Any:
    """
    Run a compliance scan on the provided data.
    
    This endpoint processes the provided compliance data, questions, and user context
    through an AI model to generate a comprehensive compliance scan report.
    
    The user_context field can contain any JSON data that provides additional context
    for the compliance scan, such as organization information, relevant regulations,
    or previous compliance history.
    
    Note: Authentication is temporarily disabled for this endpoint.
    """
    try:
        # Format the data for the compliance scanner
        formatted_data = {
            "compliance_data": "\n\n".join([item.content for item in compliance_data.compliance_data]),
            "questions": compliance_data.questions
        }
        
        # Add user context if provided
        if compliance_data.user_context:
            formatted_data["user_context"] = compliance_data.user_context
        
        # Initialize the compliance scan agent
        compliance_agent = ComplianceScanAgent()
        
        # Generate the compliance scan
        result = compliance_agent.generate_compliance_scan(formatted_data)
        
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing compliance scan: {str(e)}"
        )