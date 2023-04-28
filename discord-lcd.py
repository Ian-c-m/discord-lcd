import disnake, tokens
from rpi_lcd import LCD
from disnake.ext import commands
from time import sleep


lcd = LCD()
bot = commands.InteractionBot(test_guilds = [864438904954159104], intents=disnake.Intents.all())

@bot.event
async def on_ready():
    lcd.text('Logged into Discord!', 1)
    sleep(2)
    lcd.clear()

@bot.event
async def on_message(message: disnake.Message):
    lcd.text(f"from {message.author.name}:",1)
    lcd.text(message.content,2)
    sleep(5)
    lcd.clear()

if __name__ == "__main__":
    bot.run(tokens.discord_test_token)