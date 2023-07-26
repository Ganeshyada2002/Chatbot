import aiml
import random
import time

# Override time.clock() with time.perf_counter() for AIML library compatibility
time.clock = time.perf_counter

# Create the Kernel (AIML engine)
kernel = aiml.Kernel()

# Load the AIML files
kernel.learn("std-startup.xml")
kernel.learn("basic_chat.aiml")
kernel.learn("std-geography.aiml")  # Load the std-geography.aiml file

# Eateries dataset
eateries = ["amul", "hotspot", "thickshake factory", "yumpies", "pleasant"]

# Get a random eatery recommendation
def get_random_eatery():
    return random.choice(eateries)

# AIML-based chatbot
def get_bot_response(user_input):
    bot_response = kernel.respond(user_input)
    return bot_response

# Function to fetch geography-related data (Assuming std-geography.aiml contains appropriate patterns and templates)
def get_geography_data(user_input):
    # Fetch data from std-geography.aiml using AIML Kernel
    geography_data = kernel.respond(user_input)
    return geography_data

# Main function for conversation
def main():
    print("Bot: Hi, what's your name?")
    user_name = input("User: ")
    print(f"Bot: Hi {user_name}, how are you?")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        bot_response = get_bot_response(user_input)
        print(f"Bot: {bot_response}")

        if "eateries" in user_input.lower() or "places to eat" in user_input.lower():
            print("Bot: I can let you know some nearby eateries in BITS Hyderabad.")
            print("Bot: Here are some eateries: " + ", ".join(eateries))
            print("Bot: Would you like more information about any specific eatery?")
            user_choice = input("User: ")
            if user_choice.lower() in eateries:
                print(f"Bot: I have some recommendations for {user_choice}.")
                print(f"Bot: I recommend trying {get_random_eatery()}.")
            else:
                print("Bot: Alright! Let me know if you need any other assistance.")
        elif "geography" in user_input.lower():
            print("Bot: I can provide information about geography. What do you want to know?")
            # Fetch geography-related data using the get_geography_data function
            geography_data = get_geography_data(user_input)
            print(f"Bot: {geography_data}")
        else:
            # Use AIML-based response as a fallback
            pass

if __name__ == "__main__":
    main()
