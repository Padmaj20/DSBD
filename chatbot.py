import random

# Responses stored in a dictionary with keywords as keys
responses = {
    "hello": ["Hello! How can I assist you today?", "Hi there! How can I help you?"],
    "order status": ["Please provide your order number, and I'll check the status for you.", "Can you share your order ID?"],
    "return": ["You can return items within 30 days of purchase. Would you like more details?", "Our return policy allows returns within 30 days."],
    "shipping": ["Standard shipping takes 5-7 business days. We also offer expedited options.", "Shipping typically takes a week. Expedited shipping is available!"],
    "payment": ["Are you having trouble with payment? I can help with that.", "Is there an issue with your payment method?"],
    "thanks": ["You're welcome! If you have any other questions, feel free to ask.", "Happy to help! Let me know if there's anything else."],
    "fallback": ["I'm sorry, I didn't understand that. Could you please rephrase?", "I'm here to help! Could you clarify your question?"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Check for keywords in user input and respond accordingly
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # Default response if no keywords match
    return random.choice(responses["fallback"])

# Run the chatbot in a loop to simulate conversation
print("Welcome to the Customer Support Chatbot! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Thank you for visiting! Have a great day!")
        break
    print("Chatbot:", chatbot_response(user_input))