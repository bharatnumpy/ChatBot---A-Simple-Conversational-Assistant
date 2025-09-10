def chatbot():
    print("SimpleBot: Hello! I'm your assistant. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("SimpleBot: Hello there! How can I help you today?")
        
        elif "your name" in user_input:
            print("SimpleBot: I'm SimpleBot, your friendly assistant.")
        
        elif "how are you" in user_input:
            print("SimpleBot: I'm just a bunch of code, but I'm functioning well! How about you?")
        
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"SimpleBot: The current time is {now}")
        
        elif "date" in user_input:
            from datetime import date
            today = date.today().strftime("%B %d, %Y")
            print(f"SimpleBot: Today's date is {today}")
        
        elif "bye" in user_input:
            print("SimpleBot: Goodbye! Have a great day!")
            break
        
        else:
            print("SimpleBot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
chatbot()
