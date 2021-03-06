from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command(name="idea", help="Get a side project idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")
    await ctx.send("Worry not, I think you should...")

    topics = ['chat bot', 'cli', 'game', 'web bot', 'browser extention', 'api', 'web interface']
    areas = ['not taking', 'social life', 'physical fitness', 'mental health', 'pet care']
    language = ['C++', 'Java', 'JavaScript', 'Python', 'Rust', 'R', 'Kotlin']

    idea = f'Create a new {random.choice(topics)} that helps with {random.choice(areas)} in {random.choice(language)}! :slight_smile:'
    await ctx.send(idea)

@bot.command(name="calc", help="Perform a calculation where fn is either +,-,*, or /")
async def calc(ctx, x: float, fn: str, y: float):
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    elif fn == '**':
        await ctx.send(x ** y)
    else:
        await ctx.send("We only support 5 function operations")
   
    

with open("BOT_TOKEN.TXT", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)