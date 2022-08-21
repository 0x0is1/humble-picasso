import discord

def draw_embed(keyword, ids, c_idx):
    text = ''
    for i in ids:
        text += f'-{i}'
    text += f'-{c_idx}'
    embed = discord.Embed(title="Humble Picasso", color=0xb0e0e6)
    embed.add_field(
        name=f"{keyword}", value=f'[`](https://www.example.com/?id={text})', inline=True)
    try:
        embed.set_image(url=f'https://i.imgur.com/{ids[c_idx]}.jpg')
    except IndexError:
        embed.set_image(url=f'https://i.imgur.com/{ids[c_idx-1]}.jpg')
    return embed


def draw_embed2(keyword, filename):
    embed = discord.Embed(title="Humble Picasso", color=0xb0e0e6)
    embed.add_field(name='`Sorry for incovenience`',
                    value="I know it's very frustrating to not have multiple view option but looks like we have gone out of rate limit as Imgur do not let us upload more images as of now. It will be over soon!", inline=True)
    embed.set_image(url=f'attachment://{filename}.jpg')
    return embed
