import discord

def draw_embed(keyword, ids, c_idx, author):
    text = ''
    for i in ids: text += f'-{i}'
    text += f'-{c_idx}'
    embed = discord.Embed(title="Humble Picasso", color=0xb0e0e6)
    embed.add_field(
        name=f"{keyword}", value=f'[.](https://www.example.com/?id={text})', inline=True)
    try:
        embed.set_image(url=f'https://i.imgur.com/{ids[c_idx]}.jpg')
    except IndexError:
        embed.set_image(url=f'https://i.imgur.com/{ids[c_idx-1]}.jpg')
    embed.set_footer(text=f"Requested by {author.name}", icon_url=author.avatar.url)
    return embed


def draw_embed2(keyword, filename, author):
    embed = discord.Embed(title="Humble Picasso", color=0xb0e0e6)
    embed.add_field(name='`Sorry for incovenience`',
                    value="Imgur has 50 images per hour limit,\nso you will have only one image at once :'(", inline=True)
    embed.set_image(url=f'attachment://{filename}.jpg')
    embed.set_footer(text=f"Requested by {author.name}", icon_url=author.avatar.url)
    return embed

def draw_embed3(keyword, author):
    loading_gif_url = 'https://miro.medium.com/max/1400/1*CsJ05WEGfunYMLGfsT2sXA.gif'
    embed = discord.Embed(title="Humble Picasso", color=0xb0e0e6)
    embed.add_field(name='`Working on it...`',
                    value="Dreaming your imagination, This may take up to 20 second to 1 min.", inline=True)
    embed.set_image(url=loading_gif_url)
    embed.set_footer(
        text=f"Requested by {author.name}", icon_url=author.avatar.url)
    return embed
