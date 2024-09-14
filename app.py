from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Chatbot",
    version="1.0",
    description="A Chatbot using Gemma for Essay and Llama2 for Poem"
)

# LLM models from Ollama
gemma_llm = Ollama(model="gemma")
llama2_llm = Ollama(model="wizardlm2")

# Define prompt templates for essay and poem
essay_prompt_template = ChatPromptTemplate.from_template("Write an essay about {topic} with 100 words.")
poem_prompt_template = ChatPromptTemplate.from_template("Write a poem about {topic} for a 5-year-old child with 100 words.")

# Add route for essay using Gemma model
@app.post("/essay")
async def generate_essay(input: dict):
    topic = input.get("topic", "")
    essay_prompt = essay_prompt_template.format(topic=topic)
    result = gemma_llm(essay_prompt)
    return {"output": result}

# Add route for poem using Llama2 model
@app.post("/poem")
async def generate_poem(input: dict):
    topic = input.get("topic", "")
    poem_prompt = poem_prompt_template.format(topic=topic)
    result = llama2_llm(poem_prompt)
    return {"output": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
