import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre_archivo=archivo.filename
            url_archivo=archivo.url
            await archivo.save(f"./img/{nombre_archivo}")
            await ctx.send(f"{modelo(model_path="keras_model.h5",labels_path="labels.txt",img_path=f"./img/{nombre_archivo}")}")
    else:
        await ctx.send(f"El mensaje no contiene archivos o imagenes")


bot.run("YOUR KEY HERE")