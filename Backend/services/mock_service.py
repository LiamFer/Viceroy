import json
import os
from typing import List
from models.mock_model import MockModel

STORAGE_PATH = "storage/mocks.json"

class MockService:
    def __init__(self):
        if not os.path.exists(STORAGE_PATH):
            with open(STORAGE_PATH, "w") as f:
                json.dump([], f)

    def _read(self) -> List[dict]:
        with open(STORAGE_PATH, "r") as f:
            return json.load(f)

    def _write(self, data: List[dict]):
        with open(STORAGE_PATH, "w") as f:
            json.dump(data, f, indent=4)

    def list_mocks(self) -> List[MockModel]:
        return [MockModel(**m) for m in self._read()]

    def create_mock(self, mock: MockModel) -> MockModel:
        data = self._read()
        mock.id = len(data) + 1
        data.append(mock.dict())
        self._write(data)
        return mock

    def delete_mock(self, mock_id: int):
        data = self._read()
        data = [m for m in data if m["id"] != mock_id]
        self._write(data)
