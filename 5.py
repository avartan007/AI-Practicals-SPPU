# EXPERIMENT NO. 5
# Aim: Develop an elementary chatbot for any suitable customer interaction application

import random

# Variables with response content
name = "Bot Number 286"
monsoon = "rainy"
mood = "Smiley"

# Dictionary of responses
resp = {
    "what's your name?": [
        "They call me {0}".format(name),
        "I usually go by {0}".format(name),
        "My name is the {0}".format(name)
    ],
    "what's today's weather?": [
        "The weather is {0}".format(monsoon),
        "It's {0} today".format(monsoon)
    ],
    "how are you?": [
        "I am feeling {0}".format(mood),
        "{0}! How about you?".format(mood),
        "I am {0}! How about yourself?".format(mood)
    ],
    "": [
        "Hey! Are you there?",
        "What do you mean by these?"
    ],
    "default": [
        "This is a default message"
    ]
}

# Function to fetch response based on input
def res(message):
    if message in resp:
        bot286_message = random.choice(resp[message])
    else:
        bot286_message = random.choice(resp["default"])
    return bot286_message

# Function to determine related text
def real(xtext):
    if "name" in xtext:
        ytext = "what's your name?"
    elif "monsoon" in xtext or "weather" in xtext:
        ytext = "what's today's weather?"
    elif "how are" in xtext:
        ytext = "how are you?"
    else:
        ytext = ""
    return ytext

# Function to send and print response
def send_message(message):
    print((message))
    response = res(message)
    print((response))

# Main chatbot loop
print("BOT: Hello! What is your name?")
user_name = input("You: ")
print(f"BOT: Hi {user_name}, how can I help you today? (Type 'exit' or 'stop' to quit)")

while True:
    my_input = input("You: ")
    my_input = my_input.lower()
    if my_input == "exit" or my_input == "stop":
        print("BOT: Thank you! Have a nice day!")
        break
    related_text = real(my_input)
    send_message(related_text)
