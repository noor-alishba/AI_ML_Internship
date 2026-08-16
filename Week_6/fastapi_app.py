from fastapi import FastAPI
from a2wsgi import WSGIMiddleware

from app import app as flask_app


app = FastAPI(
    title="Heart Disease Prediction API",
    version="1.0"
)

app.mount(
    "/",
    WSGIMiddleware(flask_app)
)