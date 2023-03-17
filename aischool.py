import openai
import telebot
import os

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up Telegram bot
bot = telebot.TeleBot("5751949424:AAHXCvNBPrhAA-Az8Y7WfQ-aCYzt8U0LdIw")

# Define a dictionary to store user input
user_data = {}

# Define function to get AI response
def get_ai_response(user_input):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": f"You are AI for help students in shcool, this your mission, if any body ask you for some thing not for shcool dont repond or say Im sorry but I am not for that, your devloper is khalid aghrini, you dont have a name, can evre body call you my shcool assistant, you can remember any thing or  user information from {user_data}. \n\nQ: {user_input} \nA: "}
      ]
    )
    return completion.choices[0].message.content

# Define message handler for the bot
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Get user input and chat id
    user_input = message.text
    chat_id = message.chat.id

    # If user has provided input before, retrieve it from user_data dictionary
    if user_input in user_data:
        bot_response = user_data[user_input]
    # If user is providing input for the first time, get AI response and store it in user_data dictionary
    else:
        ai_response = get_ai_response(user_input)
        bot_response = f"{ai_response}"
        user_data[user_input] = bot_response

    # Send bot response to user
    bot.send_message(chat_id=chat_id, text=bot_response)

# Start the bot
bot.polling()
