from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.routes import routers as v1_routers

from app.core.config import configs
from app.core.container import Container
from app.util.pattern import singleton

@singleton
class App(FastAPI):
    def __init__(self):
        self.app: FastAPI = FastAPI(
            title=configs.PROJECT_NAME,
            openapi_url=None,
            redoc_url=None,
            version="0.1.0",
        )

        self.container = Container()
        self.db = self.container.db()

        # cors
        if configs.CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in configs.CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"]
            )

        @self.app.get("/")
        def root():
            return {"message": configs.PROJECT_NAME}
        
        self.app.include_router(v1_routers, prefix=configs.API_V1_STR)
        
app_instance = App()
app = app_instance.app