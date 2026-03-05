from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

# Read API key from file
with open("api_key.txt", "r") as f:
    line = f.read().strip()
    # Remove variable name and quotes
    api_key = line.split("=")[1].replace('"', '')

# Initialize client
client = OpenAI(api_key=api_key)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Code Reviewer is running"}

@app.post("/review-code")
async def review_code(
    file: UploadFile = File(None),
    code: str = Form(None)
):
    if file:
        content = (await file.read()).decode()
    elif code:
        content = code
    else:
        return {"error": "No code provided"}

    prompt = f"""
    You are a senior software engineer.
    
    Review the following code and provide:
    
    1. Bugs or logical issues
    2. Performance improvements
    3. Security concerns
    4. Code quality improvements
    5. Refactored version of the code

    Code:
{content}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return {
        "review": response.choices[0].message.content
    }