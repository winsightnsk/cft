from dotenv import load_dotenv
import uvicorn
from envloader import Env
from assignment import TEXT_ASSIGNMENT
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

load_dotenv()

app = FastAPI(
    title='shift_app',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

env: Env = Env()

@app.get("/")
def root():
    return TEXT_ASSIGNMENT

if __name__ == '__main__':

    if env.debug:
        uvicorn.run(app, host="0.0.0.0", port=8002)
