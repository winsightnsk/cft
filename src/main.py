from dotenv import load_dotenv
from src.envloader import DSL
from src.assignment import TEXT_ASSIGNMENT
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

load_dotenv()

app = FastAPI(
    title='shift_app',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.get("/")
def root():
    return TEXT_ASSIGNMENT
