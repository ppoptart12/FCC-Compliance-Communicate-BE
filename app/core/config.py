import os
from typing import Dict, Any, List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration dictionary
config: Dict[str, Any] = {
    "PROJECT_NAME": "FCC-Compliance-Communicate-BE",
    "API_V1_STR": "/api/v1",
    "SECRET_KEY": os.getenv("SECRET_KEY", "your-secret-key-for-development"),
    "ACCESS_TOKEN_EXPIRE_MINUTES": int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")),
    "ALGORITHM": "HS256",
    
    # CORS
    "ORIGINS": os.getenv("ORIGINS", "*").split(","),
    
    # Database
    "DATABASE_URL": os.getenv("DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/communicate"),
    
    # JWT
    "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key-for-development"),
    "JWT_ALGORITHM": "HS256",
    "JWT_EXPIRATION_TIME": 60 * 24,  # 24 hours
    
    # OpenAI
    "OPENAI_KEY": os.getenv("OPENAI_KEY", ""),
    "OPENAI_LLM_MODEL": os.getenv("OPENAI_LLM_MODEL", "gpt-4o"),
    "AGENT_TEMPERATURE": float(os.getenv("AGENT_TEMPERATURE", "0.7")),
    
    # Version
    "PROJECT_VERSION": "1.0.0"
}


def get(key: str, default=None) -> Any:
    """Get a configuration value."""
    return config.get(key, default) 