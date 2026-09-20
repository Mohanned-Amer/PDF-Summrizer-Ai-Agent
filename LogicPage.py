import os
import json
import uuid

import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter

from pypdf import PdfReader

# =========================================================
# Environment
# =========================================================

load_dotenv()

# =========================================================
# OpenRouter API
# =========================================================

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY is missing. "
        "Please add it to your .env file."
    )

llm = ChatOpenRouter(
    model="openrouter/free",
    temperature=0,
    api_key=API_KEY
)

# =========================================================
# Database File
# =========================================================

DB_FILE = "DataBase.json"

# =========================================================
# Local User
# =========================================================

LOCAL_USER_ID = "local_user"

# =========================================================
# Conversation ID
# =========================================================

def create_conversation_id():
    return str(uuid.uuid4())

# =========================================================
# Generate Conversation Title
# =========================================================

def generate_title(user_input):

    prompt = PromptTemplate.from_template(
        """
        Create a short and clear title for a study conversation.

        The title must:
        - Be between 2 and 6 words.
        - Describe the main study topic.
        - Not contain quotes.
        - Not contain explanations.

        User message:
        {user_input}

        Title:
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "user_input": user_input
        }
    )

    return response.content.strip()

# =========================================================
# Study AI Agent
# =========================================================

def study_agent(
    user_input,
    pdf_text=None,
    response_language="Auto Detect"
):

    if pdf_text:

        prompt_text = f"""
You are Study AI Agent, an educational assistant.

Your job is to help the student understand the uploaded study material.

Use ONLY the information available in the PDF when answering questions
about the document.

If the answer cannot be found in the PDF, clearly say that the information
is not available in the uploaded document.

Answer clearly and simply.

Response language:
{response_language}

PDF Content:
{pdf_text}

Student Question:
{user_input}

Answer:
"""

    else:

        prompt_text = f"""
You are Study AI Agent, a helpful educational assistant.

Help the student understand academic topics clearly and simply.

Response language:
{response_language}

Student Question:
{user_input}

Answer:
"""

    response = llm.invoke(
        prompt_text
    )

    return response.content.strip()

# =========================================================
# Extract PDF Text
# =========================================================

def extract_pdf_text(uploaded_file):

    try:

        reader = PdfReader(
            uploaded_file
        )

        pages_text = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages_text.append(text)

        pdf_text = "\n\n".join(
            pages_text
        )

        return pdf_text.strip()

    except Exception as e:

        raise Exception(
            f"Could not read PDF: {e}"
        )

# =========================================================
# Summarize PDF
# =========================================================

def summarize_pdf(
    pdf_text,
    response_language="Auto Detect"
):

    prompt = f"""
You are an educational AI assistant.

Summarize the following PDF study material.

Requirements:

- Focus on the important ideas.
- Keep the explanation organized.
- Use clear and simple language.
- Do not add information that is not in the document.
- Use headings and bullet points when useful.
- Make the summary useful for studying and revision.

Response language:
{response_language}

PDF Content:
{pdf_text}

Summary:
"""

    response = llm.invoke(
        prompt
    )

    return response.content.strip()

# =========================================================
# Generate Quiz
# =========================================================

def generate_quiz(
    pdf_text,
    number_of_questions,
    response_language="Auto Detect"
):

    prompt = f"""
You are an educational AI assistant.

Create a multiple-choice quiz from the following PDF study material.

Number of questions:
{number_of_questions}

Strict requirements:

1. Generate exactly {number_of_questions} questions.
2. Each question must have exactly 4 options.
3. Label the options:
   A)
   B)
   C)
   D)
4. Provide the correct answer after every question.
5. Questions must be based ONLY on the PDF.
6. Do not invent information.
7. Questions should cover important parts of the document.
8. Make the questions suitable for students.
9. Use clear and simple language.
10. Do not add questions outside the document.

Response language:
{response_language}

PDF Content:
{pdf_text}

Quiz:
"""

    response = llm.invoke(
        prompt
    )

    return response.content.strip()

# =========================================================
# Load Database
# =========================================================

def load_database():

    if not os.path.exists(
        DB_FILE
    ):

        return {
            "conversations": {
                LOCAL_USER_ID: {}
            }
        }

    try:

        with open(
            DB_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        if "conversations" not in data:

            data["conversations"] = {}

        if LOCAL_USER_ID not in data["conversations"]:

            data["conversations"][LOCAL_USER_ID] = {}

        return data

    except Exception:

        return {
            "conversations": {
                LOCAL_USER_ID: {}
            }
        }

# =========================================================
# Save Database
# =========================================================

def save_database(data):

    with open(
        DB_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )

# =========================================================
# Load Conversations
# =========================================================

def load_conversations(user_id=LOCAL_USER_ID):

    data = load_database()

    return data[
        "conversations"
    ].get(
        LOCAL_USER_ID,
        {}
    )

# =========================================================
# Create Conversation
# =========================================================

def create_conversation(
    user_id,
    first_message
):

    data = load_database()

    conversation_id = create_conversation_id()

    title = generate_title(
        first_message
    )

    if LOCAL_USER_ID not in data["conversations"]:

        data["conversations"][LOCAL_USER_ID] = {}

    data["conversations"][LOCAL_USER_ID][
        conversation_id
    ] = {

        "title": title,

        "messages": []
    }

    save_database(
        data
    )

    return conversation_id

# =========================================================
# Update Conversation
# =========================================================

def update_conversation(
    user_id,
    conversation_id,
    messages
):

    data = load_database()

    if LOCAL_USER_ID not in data["conversations"]:

        data["conversations"][LOCAL_USER_ID] = {}

    if conversation_id not in data["conversations"][LOCAL_USER_ID]:

        first_message = ""

        if messages:

            first_message = messages[0].get(
                "content",
                "Study Conversation"
            )

        data["conversations"][LOCAL_USER_ID][
            conversation_id
        ] = {

            "title": generate_title(
                first_message
            ),

            "messages": []
        }

    data["conversations"][LOCAL_USER_ID][
        conversation_id
    ]["messages"] = messages

    save_database(
        data
    )

# =========================================================
# Save Conversation
# =========================================================

def save_conversation(
    user_id,
    conversation_id,
    messages
):

    if not messages:

        return conversation_id

    if not conversation_id:

        conversation_id = create_conversation(
            LOCAL_USER_ID,
            messages[0]["content"]
        )

    update_conversation(
        LOCAL_USER_ID,
        conversation_id,
        messages
    )

    return conversation_id
