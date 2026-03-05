````markdown
# AI Code Reviewer

A web app that reviews your code using OpenAI’s API. It analyzes code files and provides automated feedback on readability, structure, and best practices.

## Step 1: Clone the Project

````

## Step 2: Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
# Activate on Windows:
.\venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
```

## Step 3: Add Your OpenAI API Key

1. Create a file named `api_key.txt` in the project folder.
2. Add your API key like this:

```text
api_key="YOUR_OPENAI_API_KEY"
```

## Step 4: Install Required Packages

Add a `requirements.txt` file in the project folder with these contents:

```
fastapi==0.111.1
uvicorn[standard]==0.23.2
openai==1.29.0
python-multipart==0.0.6
PyPDF2==3.1.1
```

Then run:

```bash
pip install -r requirements.txt
```

## Step 5: Run the App

```bash
uvicorn main:app --reload
```

This will start the server at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Step 6: Use the API

1. Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
2. Use the `/review-code` endpoint to upload your code file.
3. The API will return a review of your code.

## Notes

* Ensure your OpenAI API key has sufficient quota to avoid errors.
* You can switch models in the code (e.g., `gpt-3.5-turbo`) for faster responses and lower costs.

