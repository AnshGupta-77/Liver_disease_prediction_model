"""
Entry point for the FastAPI backend server.
"""
import uvicorn
import os

if __name__ == "__main__":
    # Run the FastAPI app
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
