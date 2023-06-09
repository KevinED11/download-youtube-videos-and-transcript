import os


from dotenv import load_dotenv


def load_config() -> dict:
    load_dotenv()
    return {"openai_api_key": os.getenv("OPENAI_API_KEY")}


