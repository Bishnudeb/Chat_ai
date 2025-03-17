import json
import random
import re

def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

def Chat(user_input, data):
    user_input = user_input.strip().lower()  # Convert input to lowercase

    # Check for exact match first
    for key in data.keys():
        if user_input == key.lower():
            return random.choice(data[key])

    # Use regex to find best match
    for key in data.keys():
        pattern = r'\b' + re.escape(key.lower()) + r'\b'
        if re.search(pattern, user_input):
            return random.choice(data[key])

    # Custom responses for specific words (flexible matching)
    if re.search(r'\bgood\b', user_input):
        return "That's great to hear!"
    if re.search(r'\bbye\b', user_input):
        return "Goodbye! Take care!"
    if re.search(r'\bfine\b', user_input):
        return "Glad to hear that!"
    if re.search(r'\bi am\b', user_input):
        return "That's nice! How can I assist you?"

    # Default response for unknown input
    return "Sorry, I don't unders
    tand."
