from responses import RESPONSES

def simple_chatbot(user_query: str) -> str:
    # Normalize input
    query = user_query.strip().rstrip("?").lower()
    # Try to find a matching key (case‑insensitive)
    for key, answer in RESPONSES.items():
        if key.lower().rstrip("?") == query:
            return answer
    return ("Sorry, I can only answer these questions:\n  • " +
            "\n  • ".join(RESPONSES.keys()))

def main():
    print("FinanceBot ready. Ask me one of the predefined questions.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ("exit", "quit"):
            print("FinanceBot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print(f"FinanceBot: {response}")

if __name__ == "__main__":
    main()