from fastapi import FastAPI
from backend.api.upload import router as upload_router
import uvicorn



app = FastAPI()

app.include_router(upload_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)