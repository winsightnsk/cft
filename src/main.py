import uvicorn
from envloader import Env
from assignment import TEXT_ASSIGNMENT
from fastapi import FastAPI
from db import models
from db.database import engine
from fastapi.responses import ORJSONResponse
from router.v1 import user

app = FastAPI(
    title='shift_app',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

env: Env = Env()

models.dec_base.metadata.create_all(engine)

app.include_router(user.router)

@app.get("/", tags=['Постановка задачи'])
def root():
    return TEXT_ASSIGNMENT

if __name__ == '__main__':

    if env.debug:
        uvicorn.run(app, host="0.0.0.0", port=8002)
