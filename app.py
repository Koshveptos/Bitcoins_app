import fastapi 
import database
import config
import pydantic_models

api = fastapi.FastAPI()


response = {"answer":"wnswer from server"}

@api.get('/')
def index():
    return response