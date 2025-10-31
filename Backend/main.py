from fastapi import FastAPI
from api import routes_mocks
from services.mock_service import MockService
from core.register import register_mock_route

app = FastAPI(title="Viceroy API", version="0.1.0")
service = MockService()

for mock in service.list_mocks():
    register_mock_route(app, mock)

routes_mocks.include_routes(app)

@app.get("/")
def root():
    return {"message": "Viceroy backend running 🚀"}
