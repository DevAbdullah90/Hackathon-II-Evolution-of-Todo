from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .db_init import main as init_database
from .api import auth_test, tasks
from .api.routes import categories, chat
from .core.exceptions import AgentError, ToolExecutionError, MCPError

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_test.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")
app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
app.include_router(chat.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.exception_handler(AgentError)
async def agent_error_handler(request: Request, exc: AgentError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(ToolExecutionError)
async def tool_execution_error_handler(request: Request, exc: ToolExecutionError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(MCPError)
async def mcp_error_handler(request: Request, exc: MCPError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
