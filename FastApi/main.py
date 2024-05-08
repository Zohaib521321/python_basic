from hello import app

# Run the FastAPI application using the uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)