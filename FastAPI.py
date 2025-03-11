from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(request: QueryRequest):
    response = generate_response(request.question)
    return {"response": response}

# Run the API using: uvicorn main:app --reload
