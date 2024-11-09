from fastapi import APIRouter

from app.api.v1.endpoints.role import router as role_router

routers = APIRouter()
router_list = [role_router]

for router in router_list:
    routers.include_router(router)