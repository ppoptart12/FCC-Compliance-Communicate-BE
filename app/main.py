from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints.UnAuth import auth
from app.api.v1.endpoints.UnAuth import pdf_compliance_scan
from app.api.v1.endpoints.Auth import user
from app.api.v1.endpoints.Auth import compliance_scan

# Import configuration
from app.core.config import get  # Changed from 'import config'

# Import logging configuration
from app.core.logging_config import logger

from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

origins = get("ORIGINS")  # Changed from config.get("ORIGINS")

app = FastAPI(
    title="FCC Compliance Communicate API",
    description="API for FCC compliance monitoring and communication",
    version=get("PROJECT_VERSION", "1.0.0"),  # Changed from config.get("PROJECT_VERSION", "1.0.0")
)

MODEL_NAME = 'Communicate backend'
MODEL_VERSION = 'v25.03.01'

# Log application startup
logger.info(f"Starting {MODEL_NAME} {MODEL_VERSION}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # FILL IN THE ORIGINS LATER
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,  # type: ignore
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)  # type: ignore
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,  # type: ignore
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


@app.get('/health')
def route_health(request: Request):
    res = dict()
    res['Communicate_backend'] = MODEL_VERSION
    res['apiVersion'] = MODEL_NAME + ':' + MODEL_VERSION
    res['statusCode'] = 200
    res['status'] = 'ok'
    res['error'] = None,
    res['message'] = "Communicate System is up and running",
    res['isOk'] = True
    return JSONResponse(content=res, status_code=200)


@app.get('/')
def root_route_health(request: Request):
    res = dict()
    res['Communicate_backend'] = MODEL_VERSION
    res['apiVersion'] = MODEL_NAME + ':' + MODEL_VERSION
    res['statusCode'] = 200
    res['status'] = 'ok'
    res['error'] = None,
    res['message'] = "Communicate System is up and running",
    res['isOk'] = True
    return JSONResponse(content=res, status_code=200)


@app.head('/health')
def route_health_head(request: Request):
    res = dict()
    res['Communicate_backend'] = MODEL_VERSION
    res['apiVersion'] = MODEL_NAME + ':' + MODEL_VERSION
    res['statusCode'] = 200
    res['status'] = 'ok'
    res['error'] = None,
    res['message'] = "Communicate System is up and running",
    res['isOk'] = True
    return JSONResponse(content=res, status_code=200)


@app.head('/')
def root_route_health_head(request: Request):
    res = dict()
    res['Communicate_backend'] = MODEL_VERSION
    res['apiVersion'] = MODEL_NAME + ':' + MODEL_VERSION
    res['statusCode'] = 200
    res['status'] = 'ok'
    res['error'] = None,
    res['message'] = "Communicate System is up and running",
    res['isOk'] = True
    return JSONResponse(content=res, status_code=200)


# ___________________________________________ API ROUTES ___________________________________________


app.include_router(auth.router, prefix="/api/v1/unauth")
app.include_router(pdf_compliance_scan.router, prefix="/api/v1/unauth")
app.include_router(user.router, prefix="/api/v1/auth")
app.include_router(compliance_scan.router, prefix="/api/v1/unauth")


# ___________________________________________ API ROUTES ___________________________________________
