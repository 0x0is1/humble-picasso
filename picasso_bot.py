# custom libs
from libdallemini import dallemini
from utils import embedgen as embeds
from utils import id_split as id_parser

# inbuilt and standard libs
import discord
import uuid
import io
import os
import base64
import json
import time

# error handling libs
from discord.errors import ClientException
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError, CommandNotFound

# instances
bot = commands.Bot(command_prefix="picasso ")
generator = dallemini.ImageGenerator()

client_id = os.environ.get('IMGUR_CLIENT_ID')

bot.remove_command('help')

@bot.event
async def on_ready():
    print('[*] Bot Status: Online')


@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if not user.bot and message.author == bot.user:
        await message.remove_reaction(str(reaction), user)
        channel = message.channel
        reaction = str(reaction)
        raw_sessionid = message.embeds[0].fields[0].value
        ids, curr_idx = id_parser.parse_id(raw_sessionid)
        if reaction == '⬅️' and curr_idx > 0:
            idx = curr_idx-1
        if reaction == '➡️' and curr_idx < len(ids):
            idx = curr_idx + 1
        if reaction == '❌':
            await message.delete()
            return
        keywords = message.embeds[0].fields[0].name
        draw_embed = embeds.draw_embed(keywords, ids, idx)
        await message.edit(embed=draw_embed)
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('`Unknown command`\nPlease use right command to operate. `help` for commands details.')
    if isinstance(error, CommandInvokeError):
        print(error)
        return


@bot.command(aliases=['hlp', 'h'])
async def help(ctx):
    await ctx.send("Prefix = `picasso help`\n**draw**: To draw image\n**Options**: keywords to draw")


@bot.command(aliases=['source', 'source-code', 'src'])
async def code(ctx):
    embed = discord.Embed(title="Humble Picasso", color=0xb0e0e6)
    embed.add_field(name='Code',
                    value="https://github.com/0x0is1/humble-picasso", inline=False)
    await ctx.send(embed=embed)


@bot.command(aliases=['credit', 'cred', 'creds'])
async def credits(ctx):
    embed = discord.Embed(title="Humble Picasso", color=0xb0e0e6)
    embed.add_field(name='Resources Disclaimer: ',
                    value="APIs used in this application is owned by Craiyon/HuggingFace(craiyon API), \
                        and Imgur (by making worst documentation ever? :/)", inline=False)
    embed.add_field(name='Developed by:', value='0x0is1', inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['make', 'create', 'gen', 'generate'])
async def draw(ctx, *, keywords):
    image_ids = generator.get_image(keywords, client_id)
    if type(image_ids) == list:
        draw_embed = embeds.draw_embed(keywords, image_ids, 0)
        msg = await ctx.send(embed=draw_embed)
        await msg.add_reaction('⬅️')
        await msg.add_reaction('➡️')
        await msg.add_reaction('❌')
    else:
        data = io.BytesIO(base64.b64decode(image_ids))
        filename = uuid.uuid4()
        file = discord.File(data, f'{filename}.jpg')
        draw_embed = embeds.draw_embed2(keywords, filename)
        msg = await ctx.send(embed=draw_embed, file=file)

