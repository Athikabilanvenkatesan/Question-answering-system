from typing import Annotated

from fastapi import FastAPI, Form

from transformers import pipeline

app = FastAPI()

question_answerer = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

@app.post("/QA/")
async def answer(question: Annotated[str, Form()], context: Annotated[str, Form()]):
    result = question_answerer(question=question, context=context)
    return {"answer": result["answer"]}
