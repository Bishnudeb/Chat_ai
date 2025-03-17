import ai

print("Loading AI module...")
data = ai.load_data()

print("AI module loaded successfully!")
print(f"Data loaded: {data}")

while True:
    user_input = input("You: ").strip()
    if not user_input:  # Avoid empty input responses
        continue
    response = ai.Chat(user_input, data)
    print(f"Ai: {response
                }")
