import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse

def register_mock_route(app: FastAPI, mock):
    route_path = mock.path
    method = mock.method.lower()

    async def dynamic_route(response_data=mock.response, status=mock.status_code, delay=mock.delay_ms):
        if delay > 0:
            time.sleep(delay / 1000)
        return JSONResponse(content=response_data, status_code=status)

    app.add_api_route(route_path, dynamic_route, methods=[method])
    print(f"[+] Added mock: {method.upper()} {route_path}")