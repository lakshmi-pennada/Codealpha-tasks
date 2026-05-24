print("🤖 Chatbot initialized! Type 'bye' to exit. 🤖\n")

# Keep the conversation going in a loop
while True:
    # Take user input and clean it up (lowercase, no extra spaces)
    user_input = input("You: ").lower().strip()
    
    # Check the rules
    if user_input in ["hello", "hi"]:
        print("Bot: Hi! How can I help you?\n")
        
    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!\n")
        
    elif user_input in ["bye", "goodbye"]:
        print("Bot: Goodbye!\n")
        break  # Exit the loop and stop the program
        
    else:
        print("Bot: I don't understand that. Try 'hello', 'how are you', or 'bye'.\n")