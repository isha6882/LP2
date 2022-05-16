# Chatbot - SIM card service provider

import random

print("BOT: What do you want me to call you?")
user_name = input()

bot_name = "Robo"
name = "Isha"
phoneNo = "9876543210"
address = "PICT, Pune"
accountNo = "12345"
balance = 110.78
data_left = 2.56

bot_template = bot_name + " : {0}"
user_template = user_name + " : {0}"

responses = {
    "What is my name registered?": [
        "Your name is {0}.".format(name),
        "You are {0}.".format(name),
        "{0} is your name.".format(name)],

    "What is my phone no?": [
        "Your phone no is {0}".format(phoneNo),
        "{0}".format(phoneNo),
        "Your mobile no is {0}".format(phoneNo), ],

    "What is my registered address?": [
        "{0}".format(address),
        "Your registered address is {0}".format(address),
        "You live at {0}".format(address), ],

    "What is my account no?": [
        "Your account no is {0}.".format(accountNo),
        "{0}".format(accountNo),
        "Account no: {0}".format(accountNo)],

    "What is my account balance?": [
        "Your account balance is Rs. {0}.".format(balance),
        "Balance: Rs. {0}".format(balance),
        "Rs. {0}".format(balance)],

    "How much mobile data is left?": [
        "{0} GB of data is left.".format(data_left),
        "Mobile data left: {0} GB".format(data_left),
        "You still have {0} GB of data left.".format(data_left)],

    "": [
        "Hey! I didn't understand you",
        "What do you mean?", ],

    "default": [
        "this is a default message"]
}


def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message


def related(x_text):
    if "name" in x_text:
        y_text = "What is my name registered?"

    elif "phone" in x_text:
        y_text = "What is my phone no?"

    elif "address" in x_text:
        y_text = "What is my registered address?"

    elif "account no" in x_text:
        y_text = "What is my account no?"

    elif "balance" in x_text:
        y_text = "What is my account balance?"

    elif "data" in x_text:
        y_text = "How much mobile data is left?"

    else:
        y_text = ""

    return y_text


def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))


print("Ask me a question")
while True:
    my_input = input()
    my_input = my_input.lower()
    related_text = related(my_input)
    send_message(related_text)

    if (my_input == "exit" or my_input == "stop"):
        break