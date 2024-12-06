from fastapi import APIRouter, HTTPException, status
import grpc
from app.generated import ml_services_pb2, ml_services_pb2_grpc

from app.core.container import Container
from app.core.middleware import inject
from app.core.config import configs

router = APIRouter(prefix="/machine-learning", tags=["machine-learning"])

GRPC_SERVER_URL = configs.GRPC_SERVER_URL

def get_grpc_channel():
    try:
        channel = grpc.secure_channel(GRPC_SERVER_URL, grpc.ssl_channel_credentials())
        grpc.channel_ready_future(channel).result(timeout=5)
        return channel
    except grpc.RpcError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Could not connect to gRPC server: {e.details()}",
        )


@router.get("/health-check", status_code=status.HTTP_200_OK)
async def health_check():
    try:
        with get_grpc_channel() as channel:
            stub = ml_services_pb2_grpc.MLServiceStub(channel)

            request = ml_services_pb2.Empty()
            response = stub.HealthCheck(request)
            return {"status": response.status}
    except grpc.RpcError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"gRPC HealthCheck error: {e.details()}",
        )

@router.post("/predict/nutrition", status_code=status.HTTP_200_OK)
@inject
def predict_nutrition():
    pass

@router.post("/predict/stunting", status_code=status.HTTP_200_OK)
@inject
def predict_stunting():
    pass