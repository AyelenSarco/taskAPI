from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from .models import task_model
from .database import  engine
from .endpoints import task,auth, users
from .exceptions.exceptions import NotFoundException, InvalidInputException, DataBaseException
from .exceptions.handlers_exceptions import not_found_exception_handler,invalid_input_exception_handler,data_base_exception_handler
task_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(task.router, tags=["tasks"])
app.include_router(auth.router, tags=["auth"])
app.include_router(users.router, tags=["users"])


app.add_exception_handler(NotFoundException, not_found_exception_handler)

app.add_exception_handler(InvalidInputException, invalid_input_exception_handler)

app.add_exception_handler(DataBaseException, data_base_exception_handler)

@app.get("/")
def root():
    print("ROOOOOOOOOT")
    return {"messege": "Running"}
