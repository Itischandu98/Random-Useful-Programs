"""
Send telegram messages using a Telegram bot
Use BotFather to create a new bot
Use @RawDataBot to get your chat_id
you first need to send the message to the above bot to be able to use the code
"""
import requests

TOKEN = "Get this token from the BotFather Details"
chat_id = "Id from RawDataBot"
message="Doesthiswork?"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())