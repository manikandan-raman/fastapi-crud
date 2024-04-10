import os

from dotenv import load_dotenv

ENVIRONEMENT = os.getenv("ENVIRONMENT", "dev")
dotenv_path = f".env.{ENVIRONEMENT}"
load_dotenv(dotenv_path=dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
