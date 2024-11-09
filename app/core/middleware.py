import asyncio
from functools import wraps
from dependency_injector.wiring import inject as di_inject
from loguru import logger
from app.service.base_service import BaseService
from fastapi import Request
from typing import Callable, Any

def inject(func: Callable[..., Any]) -> Callable[..., Any]:
    @di_inject
    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Handle both async and sync functions
        if asyncio.iscoroutinefunction(func):
            result = await func(*args, **kwargs)
        else:
            result = func(*args, **kwargs)
            
        # Get injected services
        injected_services = [
            arg for arg in kwargs.values() 
            if isinstance(arg, BaseService)
        ]
        
        if injected_services:
            try:
                # Do something with the last injected service if needed
                service = injected_services[-1]
                # Your service-related logic here
            except Exception as e:
                logger.error(f"Error in service injection: {e}")
                raise
                
        return result
    
    return wrapper