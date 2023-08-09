from discord.ext import commands
from discord.ext.commands import has_permissions
import time

client = commands.Bot(command_prefix='.')

message_list = []

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def duyuru(ctx):

    message = (str(ctx.message.content[str(ctx.message.content).find(" "):]).strip())
    if len(message)<3:
        await ctx.send("Mesaj çok kısa")
    message_list.append(message)


@client.command()
async def start(ctx):
    while True:
        for i in message_list:
            time.sleep(21600)
            await ctx.send(i)




@duyuru.error
async def duyuru_error(ctx, error):
    await ctx.send("Bu rolu kullanamazsınız...")




client.run("YourToken")