import os
import discord
from discord.ext import commands

# ---- Intents ----
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# ---- Dynamic Prefix System ----
prefixes = {}
def get_prefix(bot, message):
    return prefixes.get(message.guild.id, "!")

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

# ---- Bot Ready ----
@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}!')

# ---- Welcome Message ----
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="・txt")
    if channel:
        embed = discord.Embed(
            title="🎉 Welcome!",
            description=f"Hello {member.mention}, welcome to the server!",
            color=discord.Color.purple()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_image(url="https://media.discordapp.net/attachments/1441566592096796824/1441573456494989443/Xaviersobased.jpg")
        await channel.send(embed=embed)

# ---- Commands ----
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 Latency: {round(bot.latency * 1000)}ms", delete_after=10)

@bot.command()
@commands.has_permissions(administrator=True)
async def setprefix(ctx, new_prefix: str):
    prefixes[ctx.guild.id] = new_prefix
    await ctx.send(f"✅ Command prefix updated to: `{new_prefix}`", delete_after=10)

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

# ---- Run Bot ----
bot.run(os.getenv("TOKEN"))

