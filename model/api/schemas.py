from pydantic import BaseModel

class NotesRequest(BaseModel):
    topic : str

class NotesResponse(BaseModel):
    notes : str
    summary : str