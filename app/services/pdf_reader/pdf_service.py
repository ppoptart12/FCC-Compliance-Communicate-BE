import io
import logging
from typing import Dict, Any, Optional

import pypdf
from fastapi import UploadFile, HTTPException

logger = logging.getLogger(__name__)


class PDFService:
    """Service for handling PDF operations like text extraction."""
    
    @staticmethod
    async def extract_text_from_pdf(file: UploadFile) -> Dict[str, Any]:
        """
        Extract text from a PDF file.
        
        Args:
            file: The uploaded PDF file
            
        Returns:
            Dict containing the extracted text, filename, and page count
            
        Raises:
            HTTPException: If the file is not a PDF or text extraction fails
        """
        if not file.filename.lower().endswith('.pdf'):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed")
        
        try:
            # Read the uploaded file
            contents = await file.read()
            
            # Extract text from PDF
            pdf_reader = pypdf.PdfReader(io.BytesIO(contents))
            
            # Get total page count
            page_count = len(pdf_reader.pages)
            
            # Extract text from each page
            full_text = ""
            for page_num in range(page_count):
                try:
                    page_text = pdf_reader.pages[page_num].extract_text()
                    if page_text:  # Some pages might not have extractable text
                        full_text += f"--- Page {page_num + 1} ---\n{page_text}\n\n"
                except Exception as e:
                    logger.warning(f"Error extracting text from page {page_num + 1}: {str(e)}")
                    full_text += f"--- Page {page_num + 1} ---\n[Error extracting text from this page]\n\n"
            
            # Check if we got any text
            if not full_text.strip():
                raise HTTPException(
                    status_code=422, 
                    detail="Could not extract text from PDF. The file may be scanned or contain only images."
                )
            
            # Rewind the file for potential future use
            await file.seek(0)
            
            return {
                "filename": file.filename,
                "text": full_text,
                "page_count": page_count
            }
            
        except HTTPException:
            # Re-raise HTTP exceptions
            raise
        except Exception as e:
            logger.error(f"Error processing PDF: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")
    
    @staticmethod
    async def get_pdf_metadata(file: UploadFile) -> Optional[Dict[str, Any]]:
        """
        Extract metadata from a PDF file.
        
        Args:
            file: The uploaded PDF file
            
        Returns:
            Dict containing metadata or None if extraction fails
        """
        try:
            # Read the uploaded file
            contents = await file.read()
            
            # Get PDF metadata
            pdf_reader = pypdf.PdfReader(io.BytesIO(contents))
            metadata = pdf_reader.metadata
            
            # Rewind the file for potential future use
            await file.seek(0)
            
            if metadata:
                # Convert metadata to a regular dict with string values
                meta_dict = {}
                for key, value in metadata.items():
                    if key.startswith('/'):
                        key = key[1:]  # Remove leading slash from keys
                    meta_dict[key] = str(value)
                return meta_dict
            
            return None
            
        except Exception as e:
            logger.warning(f"Error extracting PDF metadata: {str(e)}")
            return None 