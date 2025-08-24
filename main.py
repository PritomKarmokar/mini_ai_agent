from agent.orchestrator import Orchestrator

def main():
    orchestrator = Orchestrator()
    print("Welcome to the AI Agent System. Type your query (or 'exit'):")
    while True:
        user_input = input()
        if user_input.lower() in ["exit", "quit"]:
            break
        response = orchestrator.handle(user_input)
        print("Response:", response)

if __name__ == "__main__":
    main()