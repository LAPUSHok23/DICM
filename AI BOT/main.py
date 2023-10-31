import discord
from discord.ext import commands
import os, random
import requests
from settings import TOKEN


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')

@bot.command('duck')
async def duck(ctx):
    '''По команде duck возвращает фото утки'''
    print('hello')
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            image_path = f'images/{file_name}'
            await attachment.save(image_path)
            await ctx.send(model_path="./keras_model.h5", labels_path="./labels.txt", image_path=image_path)
            print("Сохраненно")
            os.remove(image_path)
            print("Удаленнно")
        else:
            await ctx('КАРТИНКА НЕ  НАЙДЕНА ')


bot.run(TOKEN)