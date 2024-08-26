from fastapi import  Request
from fastapi.responses import JSONResponse
from .exceptions import NotFoundException, InvalidInputException, DataBaseException




async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(status_code=exc.status_code, content={"message":exc.detail})

async def invalid_input_exception_handler(request:Request, exc:InvalidInputException):
    return JSONResponse(status_code=exc.status_code, content={"message":exc.detail})

async def data_base_exception_handler(request:Request, exc:DataBaseException):
    return JSONResponse(status_code=exc.status_code, content={"message":exc.detail})
