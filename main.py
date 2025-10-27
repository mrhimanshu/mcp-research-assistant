import os
from dotenv import load_dotenv

load_dotenv(os.path.join('.env'), override=True)

def main():
    print("Hello from mcp-tutorial!")
    print(os.getenv("OPENAI_API_KEY"))

if __name__ == "__main__":
    main()
