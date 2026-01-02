# Taskoo AI: Spec-Driven Fullstack Assistant

This project implements an AI-Native Task Management Assistant, allowing users to manage their tasks through a conversational interface. The system leverages a stateless backend, an AI Agent, and Model Context Protocol (MCP) tools for robust and scalable interaction.

## Architecture

```
┌─────────────────┐     ┌──────────────────────────────────────────────┐     ┌─────────────────┐
│                 │     │              FastAPI Server                   │     │                 │
│                 │     │  ┌────────────────────────────────────────┐  │     │                 │
│  ChatKit UI     │────▶│  │         Chat Endpoint                  │  │     │    Neon DB      │
│  (Frontend)     │     │  │  POST /api/chat                        │  │     │  (PostgreSQL)   │
│                 │     │  └───────────────┬────────────────────────┘  │     │                 │
│                 │     │                  │                           │     │  - tasks        │
│                 │     │                  ▼                           │     │  - conversations│
│                 │     │  ┌────────────────────────────────────────┐  │     │  - messages     │
│                 │◀────│  │      OpenAI Agents SDK                 │  │     │                 │
│                 │     │  │      (Agent + Runner)                  │  │     │                 │
│                 │     │  └───────────────┬────────────────────────┘  │     │                 │
│                 │     │                  │                           │     │                 │
│                 │     │                  ▼                           │     │                 │
│                 │     │  ┌────────────────────────────────────────┐  │────▶│                 │
│                 │     │  │         MCP Server                 │  │     │                 │
│                 │     │  │  (MCP Tools for Task Operations)       │  │◀────│                 │
│                 │     │  └────────────────────────────────────────┘  │     │                 │
└─────────────────┘     └──────────────────────────────────────────────┘     └─────────────────┘
```

## Technology Stack

-   **Frontend**: OpenAI ChatKit (Next.js)
-   **Backend**: Python FastAPI
-   **AI Framework**: OpenAI Agents SDK
-   **MCP Server**: Official MCP SDK
-   **ORM**: SQLModel
-   **Database**: Neon Serverless PostgreSQL
-   **Authentication**: Better Auth (JWT-based)

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

-   Python 3.11+
-   Node.js 18+
-   Docker (Optional, for local PostgreSQL if not using Neon)
-   OpenAI API Key
-   Better Auth account/setup (or use local `better-auth` setup)

### 1. Backend Setup

1.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

2.  **Create and activate a Python virtual environment**:
    ```bash
    python -m venv .venv
    # On Windows:
    # .venv\Scripts\activate
    # On macOS/Linux:
    # source .venv/bin/activate
    ```

3.  **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables**:
    Copy `.env.example` to `.env` and fill in your details:
    ```bash
    cp .env.example .env
    ```
    Edit `.env` with your `DATABASE_URL`, `OPENAI_API_KEY`, and `BETTER_AUTH_SECRET`.

5.  **Initialize the database**:
    ```bash
    python -m src.db_init
    ```

6.  **Run the FastAPI backend**:
    ```bash
    uvicorn src.main:app --reload
    ```
    The backend should be running at `http://localhost:8000`.

### 2. Frontend Setup

1.  **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```

2.  **Install Node.js dependencies**:
    ```bash
    npm install
    ```

3.  **Configure environment variables**:
    Copy `.env.example` to `.env.local` and fill in your details:
    ```bash
    cp .env.example .env.local
    ```
    Edit `.env.local` with your `NEXT_PUBLIC_API_URL` (e.g., `http://localhost:8000`), `BETTER_AUTH_URL`, `BETTER_AUTH_SECRET`, and `NEXT_PUBLIC_OPENAI_DOMAIN_KEY`.

4.  **Run the Next.js frontend**:
    ```bash
    npm run dev
    ```
    The frontend should be running at `http://localhost:3000`.

## Usage

1.  Open your browser to `http://localhost:3000`.
2.  Sign up or log in using Better Auth.
3.  Navigate to the `/chat` page.
4.  Start interacting with the AI assistant! Try commands like:
    -   "Add a task to buy groceries"
    -   "List my pending tasks"
    -   "Mark task 1 as complete"
    -   "Delete task 2"

## Development Notes

-   **Stateless Backend**: The FastAPI backend does not maintain session state; conversation history is persisted in the database and loaded per request.
-   **MCP Tools**: All task management operations are exposed as Model Context Protocol (MCP) tools, which the OpenAI Agent invokes.
-   **Security**: User authentication via Better Auth and JWT ensures user isolation.