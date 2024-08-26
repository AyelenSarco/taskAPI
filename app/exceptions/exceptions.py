from fastapi import HTTPException, status

class NotFoundException (HTTPException):
    def __init__(self,message:str):
        super(NotFoundException,self).__init__(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=message
            )

class InvalidInputException(HTTPException):
    def __init__(self, message:str):
        super(InvalidInputException,self).__init__(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=message
            )

class DataBaseException(HTTPException):
    def __init__(self, message:str):
        super(DataBaseException,self).__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=message
        )

class CredentialsExceptions(HTTPException):
    def __init__(self):
        super(CredentialsExceptions,self).__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Barear"},
            )