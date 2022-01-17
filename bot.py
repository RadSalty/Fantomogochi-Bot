import discord
from discord.ext import commands
import glob
from dotenv import load_dotenv
import os
import aiohttp

load_dotenv()

# update bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialise the bot
bot = commands.Bot(command_prefix="/", help_command=None)

# client = discord.Client()

# Startup Information
@bot.event
async def on_ready():
    print("Connected to bot: {}".format(bot.user.name))
    print("Bot ID: {}".format(bot.user.id))
    # Upon joining a guild send help on how to get the information
    guild = bot.get_guild(910164456875642890)
    # await rebase.send('React to this message to get your "Rebase Watcher" Role!')
    await guild.me.edit(nick=f"fantomgochi Bot")
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
                            title=f"fantomgochi #{f_id}",
                            description=res["description"],
                            color=0xFF5733,
                        )
                        embed.set_image(url=res["image"])
                        for x in range(0, len(res["attributes"])):
                            embed.add_field(
                                name=res["attributes"][x]["trait_type"],
                                value=res["attributes"][x]["value"],
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
                            title=f"fantomgochi #{f_id}",
                            description=res["description"],
                            color=0xFF5733,
                        )
                        embed.set_image(url=res["image"])
                        for x in range(0, len(res["attributes"])):
                            embed.add_field(
                                name=res["attributes"][x]["trait_type"],
                                value=res["attributes"][x]["value"],
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
async def help(ctx):
    embed = discord.Embed(
        title=f"fantomgochi Bot Guide",
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
        name="/help",
        value="Get the list of commands",
        inline=False,
    )
    await ctx.send(embed=embed)


bot.run(BOT_TOKEN)
