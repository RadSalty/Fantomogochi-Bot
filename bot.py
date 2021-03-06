import discord
from discord.ext import commands
import glob
from dotenv import load_dotenv
import os
import aiohttp
from utilities import get_rarity

load_dotenv()

# Get Bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# load percentages
rarity = get_rarity()

# Initialise the bot
bot = commands.Bot(command_prefix="/", help_command=None)

# client = discord.Client()

# Startup Information
@bot.event
async def on_ready():
    print("Connected to bot: {}".format(bot.user.name))
    print("Bot ID: {}".format(bot.user.id))
    # Upon joining a guild send help on how to get the information
    guild = bot.get_guild(912209821078536193)
    # await rebase.send('React to this message to get your "Rebase Watcher" Role!')
    await guild.me.edit(nick=f"Fantomgochi Bot")
    embed = discord.Embed(
        title=f"Fantomgochi Bot Guide",
        description="Use the following commands to see your fantomgochi",
        color=0xFF5733,
    )
    embed.set_thumbnail(
        url="https://gateway.pinata.cloud/ipfs/QmcUBDXxDaLQnbyL6RJ9fyY5rFJ4eBBv1BQUayHDvGzb7y/1.png"
    )
    embed.add_field(
        name="/fantomgochi #",
        value="Replace # with your fantomgochi number to see the traits and an image",
        inline=False,
    )
    embed.add_field(
        name="/gochi #",
        value="Replace # with your fantomgochi number to see the traits and an image",
        inline=False,
    )
    embed.add_field(
        name="/link #",
        value="Replace # with your fantomgochi number to link to Paintswap & NFTKey",
        inline=False,
    )
    embed.add_field(
        name="/help",
        value="Get the list of commands",
        inline=False,
    )
    for guild in bot.guilds:
        for channel in guild.text_channels:
            await channel.send(embed=embed)


@bot.event
async def on_message(message):
    # INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
    await bot.process_commands(message)


@bot.command()
async def fantomgochi(ctx, f_id):
    if f_id.isnumeric() == True:
        if int(f_id) > 0 and int(f_id) <= 2019:
            try:
                async with aiohttp.ClientSession() as cs:
                    async with cs.get(
                        f"https://gateway.pinata.cloud/ipfs/QmP9U47KUJFsP2CkfKEQ5PvfLX55HGpWjWp4NXYCgnmWZM/{f_id}.json"
                    ) as r:
                        res = await r.json()
                        embed = discord.Embed(
                            title=f"Fantomgochi #{f_id}",
                            description=res["description"],
                            color=0xFF5733,
                        )
                        embed.set_image(url=res["image"])
                        for x in range(0, len(res["attributes"])):
                            embed.add_field(
                                name=res["attributes"][x]["trait_type"],
                                value=f"{res['attributes'][x]['value'].strip().replace('_',' ')} ({rarity[res['attributes'][x]['trait_type'].strip().replace('_',' ')][res['attributes'][x]['value'].strip().replace('_',' ')]:.2f}%)",
                                inline=True,
                            )
                        embed.add_field(
                            name="Atrributes Count",
                            value=f"{len(res['attributes'])} ({rarity['Attributes count'][str(len(res['attributes']))]:.2f}%)",
                            inline=True,
                        )
                        await ctx.send(embed=embed)
            except:
                await ctx.channel.send(f"Something went wrong, please try again later")
        else:
            await ctx.channel.send(
                f"Incorrect command, Please use a number between 1 and 2019"
            )
    else:
        await ctx.channel.send(
            f"Incorrect command, Please use a number between 1 and 2019"
        )


@bot.command()
async def gochi(ctx, f_id):
    if f_id.isnumeric() == True:
        if int(f_id) > 0 and int(f_id) <= 2019:
            try:
                async with aiohttp.ClientSession() as cs:
                    async with cs.get(
                        f"https://gateway.pinata.cloud/ipfs/QmP9U47KUJFsP2CkfKEQ5PvfLX55HGpWjWp4NXYCgnmWZM/{f_id}.json"
                    ) as r:
                        res = await r.json()
                        embed = discord.Embed(
                            title=f"Fantomgochi #{f_id}",
                            description=res["description"],
                            color=0xFF5733,
                        )
                        embed.set_image(url=res["image"])
                        for x in range(0, len(res["attributes"])):
                            embed.add_field(
                                name=res["attributes"][x]["trait_type"],
                                value=f"{res['attributes'][x]['value'].strip().replace('_',' ')} ({rarity[res['attributes'][x]['trait_type'].strip().replace('_',' ')][res['attributes'][x]['value'].strip().replace('_',' ')]:.2f}%)",
                                inline=True,
                            )
                        embed.add_field(
                            name="Atrributes Count",
                            value=f"{len(res['attributes'])} ({rarity['Attributes count'][str(len(res['attributes']))]:.2f}%)",
                            inline=True,
                        )
                        await ctx.send(embed=embed)
            except:
                await ctx.channel.send(f"Something went wrong, please try again later")
        else:
            await ctx.channel.send(
                f"Incorrect command, Please use a number between 1 and 2019"
            )
    else:
        await ctx.channel.send(
            f"Incorrect command, Please use a number between 1 and 2019"
        )


@bot.command()
async def link(ctx, f_id):
    if f_id.isnumeric() == True:
        if int(f_id) > 0 and int(f_id) <= 2019:
            try:
                embed = discord.Embed(
                    title=f"Fantomgochi #{f_id}",
                    description=f"View Fantomgochi #{f_id} at the following links",
                    color=0xFF5733,
                )
                embed.add_field(
                    name="Paintswap",
                    value=f"https://paintswap.finance/marketplace/assets/0x1c9d0b3eb50bf51a9723e2dcca679242b2747f03/{f_id}",
                    inline=False,
                )
                embed.add_field(
                    name="NFTKey",
                    value=f"https://nftkey.app/collections/fantomgochi/token-details/?tokenId={f_id}",
                    inline=False,
                )
                embed.set_thumbnail(
                    url=f"https://gateway.pinata.cloud/ipfs/QmcUBDXxDaLQnbyL6RJ9fyY5rFJ4eBBv1BQUayHDvGzb7y/{f_id}.png"
                )
                await ctx.send(embed=embed)
            except:
                await ctx.channel.send(f"Something went wrong, please try again later")
        else:
            await ctx.channel.send(
                f"Incorrect command, Please use a number between 1 and 2019"
            )
    else:
        await ctx.channel.send(
            f"Incorrect command, Please use a number between 1 and 2019"
        )


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title=f"Fantomgochi Bot Guide",
        description="Use the following commands to see your fantomgochi",
        color=0xFF5733,
    )
    embed.set_thumbnail(
        url="https://gateway.pinata.cloud/ipfs/QmcUBDXxDaLQnbyL6RJ9fyY5rFJ4eBBv1BQUayHDvGzb7y/1.png"
    )
    embed.add_field(
        name="/fantomgochi #",
        value="Replace # with your fantomgochi number to see the traits and an image",
        inline=False,
    )
    embed.add_field(
        name="/gochi #",
        value="Replace # with your fantomgochi number to see the traits and an image",
        inline=False,
    )
    embed.add_field(
        name="/link #",
        value="Replace # with your fantomgochi number to link to Paintswap & NFTKey",
        inline=False,
    )
    embed.add_field(
        name="/help",
        value="Get the list of commands",
        inline=False,
    )
    await ctx.send(embed=embed)


bot.run(BOT_TOKEN)
