from pydantic import BaseModel, Field

class InputMessage(BaseModel):
    message: str = Field(..., description="The message to process")
   
