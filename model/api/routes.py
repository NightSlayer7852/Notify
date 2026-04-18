from fastapi import APIRouter
from api.schemas import NotesRequest, NotesResponse
from graph import build_graph

router = APIRouter()
graph = build_graph()
@router.post("/generate", response_model= NotesResponse)
def generate_notes(request : NotesRequest):
    result = graph.invoke({
        "topic" : request
    })

    return {
        "notes" : result["notes"],
        "summary" : result["summary"]
    }