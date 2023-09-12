#12/09/2023 Alejandro Sossa proyecto bot de discord calculadora


import os 
import discord
from discord.ext import commands 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('dt')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) #Prefijo del bot

#Funcion de suma
@bot.command(name= 'suma')
async def sumar(ctx, a, b):
    response = int(a) + int(b)
    await ctx.send(response)

#Funcion de multiplicacion
@bot.command(name= 'multiplicar')
async def multiplica(ctx, a, b):
    response = int(a) * int(b)
    await ctx.send(response)

#Funcion de division
@bot.command(name= 'division')
async def dividir(ctx, a, b):
    response = int(a) / int(b)
    await ctx.send(response)

#Funcion de restar
@bot.command(name= 'resta')
async def restar(ctx, a, b):
    response = int(a) - int(b)
    await ctx.send(response)

bot.run(TOKEN)







