import uvicorn
from fastapi import FastAPI

from presentation.api import api_router

app = FastAPI(
    title="CAR API",
    summary="use this API to get scraped data of car listing from mudah.my",
)

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
    )
