import os
import discord
from discord.ext import commands
import requests
import asyncio
from dotenv import load_dotenv
load_dotenv()


async def update_activity():
    while True:
        response = requests.get('https://mempool.space/api/v1/fees/recommended')
        data = response.json()
        High_fee = data['fastestFee']
        Medium_fee = data['halfHourFee']
        low_fee = data['hourFee']
        activity = discord.Game(name=f"Low-{low_fee} Mid-{Medium_fee} High-{High_fee}")
        await bot.change_presence(activity=activity)
        await asyncio.sleep(5)

bot = commands.Bot(command_prefix='!',status=discord.Status.idle)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    bot.loop.create_task(update_activity())


bot.run(os.getenv("TOKEN"))

