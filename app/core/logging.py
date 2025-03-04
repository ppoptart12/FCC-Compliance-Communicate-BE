import logging
import sys
import json
from typing import Any, Dict, List, Optional, Union

# Create a logger
logger = logging.getLogger("fcc_compliance_api")
logger.setLevel(logging.INFO)

# Create console handler if not already added
if not logger.handlers:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def log_info(message: str) -> None:
    """Log an info message to the console."""
    logger.info(message)


def log_error(message: str) -> None:
    """Log an error message to the console."""
    logger.error(message)


def log_warning(message: str) -> None:
    """Log a warning message to the console."""
    logger.warning(message)


def log_debug(message: str) -> None:
    """Log a debug message to the console."""
    logger.debug(message)


def log_request(endpoint: str, method: str, params: Optional[Dict[str, Any]] = None) -> None:
    """Log an API request with its parameters."""
    log_info(f"Request: {method} {endpoint} - Params: {json.dumps(params) if params else 'None'}")


def log_response(endpoint: str, status_code: int, response_data: Optional[Union[Dict[str, Any], List[Any]]] = None) -> None:
    """Log an API response with its status code and data."""
    log_info(f"Response: {endpoint} - Status: {status_code} - Data: {json.dumps(response_data) if response_data else 'None'}")


def log_exception(e: Exception, context: Optional[str] = None) -> None:
    """Log an exception with optional context."""
    if context:
        log_error(f"Exception in {context}: {str(e)}")
    else:
        log_error(f"Exception: {str(e)}") 