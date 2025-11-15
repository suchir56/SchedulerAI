#!/usr/bin/env python3
"""Run the FastAPI application."""

import uvicorn
from app.config import get_settings

if __name__ == "__main__":
    settings = get_settings()

    print(f"Starting SchedulerAI API on port {settings.backend_port}...")
    print(f"API Documentation: http://localhost:{settings.backend_port}/docs")

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.backend_port,
        reload=True
    )
