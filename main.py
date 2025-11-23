import os
import discord
from discord.ext import commands

# --- Discord intents ---
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# --- Bot setup ---
bot = commands.Bot(command_prefix=";", intents=intents)

# --- Bot ready event ---
@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}!')

# --- Welcome message ---
@bot.event
async def on_member_join(member):
    # Replace "・txt" with your actual channel name
    channel = discord.utils.get(member.guild.text_channels, name="・txt")
    if channel:
        # Ping the user first
        await channel.send(f"Welcome {member.mention}!")
        # Then send embed separately
        embed = discord.Embed(
            title="🎉 Welcome!",
            description=f"Glad to have you in {member.guild.name}!",
            color=discord.Color.purple()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_image(url="https://media.discordapp.net/attachments/1441566592096796824/1441573456494989443/Xaviersobased.jpg")
        await channel.send(embed=embed)

# --- Ping command ---
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 Latency: {round(bot.latency * 1000)}ms", delete_after=10)

# --- Set prefix command ---
@bot.command()
@commands.has_permissions(administrator=True)
async def setprefix(ctx, new_prefix: str):
    bot.command_prefix = new_prefix
    await ctx.send(f"✅ Command prefix updated to: `{new_prefix}`", delete_after=10)

# --- Preview welcome embed command ---
@bot.command()
async def preview_welcome(ctx):
    embed = discord.Embed(
        title="🎉 Welcome!",
        description=f"Hello {ctx.author.mention}, welcome to the server!",
        color=discord.Color.purple()
    )
    embed.set_thumbnail(url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    embed.set_image(url="https://media.discordapp.net/attachments/1441566592096796824/1441573456494989443/Xaviersobased.jpg")
    await ctx.send(embed=embed, delete_after=10)

# --- Run bot ---
bot.run(os.environ["DISCORD_TOKEN"])
