import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

if API_KEY:
    print("✅ API Key Loaded Successfully!")
else:
    print("❌ Failed to Load API Key. Check your .env file.")