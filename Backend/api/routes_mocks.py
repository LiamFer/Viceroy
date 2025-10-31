from fastapi import APIRouter, HTTPException
from models.mock_model import MockModel
from services.mock_service import MockService
from core.register import register_mock_route

router = APIRouter(prefix="/mocks", tags=["Mocks"])
service = MockService()

@router.get("/")
def list_mocks():
    return service.list_mocks()

# recebe app como parâmetro na criação do router
def include_routes(app):
    @router.post("/")
    def create_mock(mock: MockModel):
        new_mock = service.create_mock(mock)
        register_mock_route(app, new_mock)  # app passado aqui
        return new_mock

    @router.delete("/{mock_id}")
    def delete_mock(mock_id: int):
        service.delete_mock(mock_id)
        return {"message": "Mock deleted"}

    app.include_router(router)
