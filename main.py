import sys
import os
from agent.agent import answer
from confg.loadenv import load_env

def main():
    load_env()
    print(os.getenv("GEMINI_API_KEY"))
    if len(sys.argv) < 2:
        print("Usage: python main.py \"your question here\"")
        sys.exit(1)
    q = " ".join(sys.argv[1:])
    out = answer(q)
    print(out)

if __name__ == "__main__":
    main()
