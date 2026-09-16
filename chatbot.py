import re


# 1. TEXT NORMALIZATION

def normalize_text(text):
    """
    Convert user input into a clean, lowercase format.
    Removes unnecessary special characters.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# 2. CHATBOT RESPONSES

responses = {

    "greeting": [
        "Hello! How can I help you today?",
        "Hi! Nice to meet you.",
        "Hey! What would you like to know?"
    ],

    "python": (
        "Python is a high-level programming language known "
        "for its simple syntax and wide range of applications."
    ),

    "variables": (
        "A variable is used to store data in Python. "
        "Example: name = 'Aimen'"
    ),

    "functions": (
        "A function is a reusable block of code that performs "
        "a specific task. It is created using the def keyword."
    ),

    "loops": (
        "Python mainly provides for and while loops. "
        "They are used to repeat a block of code."
    ),

    "automation": (
        "Python automation means using Python scripts to "
        "perform repetitive tasks automatically."
    ),

    "help": (
        "I can help you with Python, variables, functions, "
        "loops, automation, or general information."
    ),

    "goodbye": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Thanks for chatting. Goodbye!"
    ]
}


# 3. INTENT KEYWORDS

intent_keywords = {

    "greeting": [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ],

    "python": [
        "python",
        "what is python",
        "tell me about python"
    ],

    "variables": [
        "variable",
        "variables",
        "what is a variable"
    ],

    "functions": [
        "function",
        "functions",
        "what is a function"
    ],

    "loops": [
        "loop",
        "loops",
        "for loop",
        "while loop"
    ],

    "automation": [
        "automation",
        "automate",
        "automated"
    ],

    "help": [
        "help",
        "what can you do",
        "options",
        "menu"
    ],

    "goodbye": [
        "bye",
        "goodbye",
        "exit",
        "quit",
        "see you"
    ]
}


# 4. INTENT DETECTION

def detect_intent(user_input):
    """
    Identify the user's intent using keyword matching.
    """

    for intent, keywords in intent_keywords.items():

        for keyword in keywords:

            if keyword in user_input:
                return intent

    return "unknown"


# 5. RESPONSE HANDLER

def get_response(intent, session):

    if intent == "greeting":

        return responses["greeting"][
            session["greeting_count"] % len(responses["greeting"])
        ]

    elif intent == "python":

        session["topic"] = "python"
        return responses["python"]

    elif intent == "variables":

        session["topic"] = "python"
        return responses["variables"]

    elif intent == "functions":

        session["topic"] = "python"
        return responses["functions"]

    elif intent == "loops":

        session["topic"] = "python"
        return responses["loops"]

    elif intent == "automation":

        session["topic"] = "automation"
        return responses["automation"]

    elif intent == "help":

        return responses["help"]

    elif intent == "goodbye":

        return responses["goodbye"][
            session["goodbye_count"] % len(responses["goodbye"])
        ]

    else:

        return (
            "Sorry, I didn't understand that. "
            "You can ask me about Python, variables, functions, "
            "loops, automation, or type 'help'."
        )


# 6. SESSION STATE

def create_session():
    """
    Create and maintain chatbot session information.
    """

    return {
        "topic": None,
        "greeting_count": 0,
        "goodbye_count": 0,
        "message_count": 0
    }


# 7. MAIN CHATBOT LOOP

def run_chatbot():

    session = create_session()

    print("=" * 50)
    print("        PYTHON RULE-BASED CHATBOT")
    print("=" * 50)

    print("\nBot: Hello! I'm your Python assistant.")
    print("Bot: Type 'help' to see what I can do.")
    print("Bot: Type 'bye' or 'exit' to end the conversation.\n")

    while True:

        user_input = input("You: ")

        # Normalize input
        normalized_input = normalize_text(user_input)

        # Empty input handling
        if not normalized_input:

            print("Bot: Please enter a message.")
            continue

        # Update session
        session["message_count"] += 1

        # Detect intent
        intent = detect_intent(normalized_input)

        # Handle response
        response = get_response(intent, session)

        print(f"Bot: {response}")

        # Update counters
        if intent == "greeting":

            session["greeting_count"] += 1

        elif intent == "goodbye":

            session["goodbye_count"] += 1
            break


# 8. PROGRAM START

if __name__ == "__main__":
    run_chatbot()