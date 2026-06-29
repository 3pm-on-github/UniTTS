import discord
import dotenv # type: ignore
import os
from gtts import gTTS

dotenv.load_dotenv()
bot = discord.Client(intents=discord.Intents.all())
vc = None

@bot.event
async def on_ready():
    global vc
    print("UniTTS is online!")
    guild = bot.get_guild(1437258836896514212)
    voice_channel = guild.get_channel(1437271857140076606)
    vc = await voice_channel.connect()

@bot.event
async def on_message(msg):
    if msg.author.bot or msg.channel.id != 1437271857140076606:
        return
    
    if msg.content.startswith("$"):
        message = msg.content[1:].strip()
        tts = gTTS(message)
        tts.save(f"{str(msg.id)}.mp3")
        def after(_):
            os.remove(f"{str(msg.id)}.mp3")
        vc.play(discord.FFmpegPCMAudio(source=f"{str(msg.id)}.mp3"), after=after)
    elif msg.content == "MI BOMBO":
        vc.play(discord.FFmpegPCMAudio(source="mibombo.mp3"))

bot.run(os.getenv("BOT_TOKEN"))