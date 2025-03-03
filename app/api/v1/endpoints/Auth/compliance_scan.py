from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.utils.auth import get_current_user
from app.schemas.compliance_scan import ComplianceScanRequest, ComplianceScanResponse
from app.services.compliance_scan.compliance_scanner import ComplianceScanAgent

router = APIRouter()


@router.post("/compliance_scan", response_model=ComplianceScanResponse)
def run_compliance_scan(
    *,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    compliance_data: ComplianceScanRequest
) -> Any:
    """
    Run a compliance scan on the provided data.
    
    This endpoint processes the provided compliance data and questions
    through an AI model to generate a compliance scan report.
    """
    try:
        # Format the data for the compliance scanner
        formatted_data = {
            "compliance_data": "\n\n".join([item.content for item in compliance_data.compliance_data]),
            "questions": compliance_data.questions
        }
        
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