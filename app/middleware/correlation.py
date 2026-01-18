import uuid
from fastapi import Request

async def correlation_middleware(request: Request, call_next):
    correlation_id = request.headers.get(
        "X-Correlation-Id",
        str(uuid.uuid4())
    )
    request.state.correlation_id = correlation_id

    response = await call_next(request)
    response.headers["X-Correlation-Id"] = correlation_id
    return response
