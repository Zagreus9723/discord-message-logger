import discord
from discord.ext import commands
import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
bot = commands.Bot(command_prefix='.', self_bot=True)
bot.remove_command("help")
@bot.event
async def on_message_delete(message):
    try:
        webhook = DiscordWebhook(
        url="WEBHOOK_HERE",
        rate_limit_retry=True)
        embed = DiscordEmbed(title='Message deleted')
        embed.set_author(name=f"{message.author}")
        embed.add_embed_field(name="Message", value=f"{message.content}")
        embed.add_embed_field(name="Guild", value=f"{message.guild.name}")
        embed.add_embed_field(name="Channel", value=f"{message.channel.mention}")
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        webhook = DiscordWebhook(
            url="WEBHOOK_HERE",
            rate_limit_retry=True)
        embed = DiscordEmbed(title='DM deleted')
        embed.set_author(name=f"{message.author}")
        embed.add_embed_field(name="Message", value=f"{message.content}")
        webhook.add_embed(embed)
        response = webhook.execute()

@bot.event
async def on_message_edit(message_before, message_after):
    if f"{message_before.content}" != f"{message_after.content}":
        try:
            webhook = DiscordWebhook(
            url="WEBHOOK_HERE",
            rate_limit_retry=True)
            embed = DiscordEmbed(title='Message edited')
            embed.set_author(name=f"{message_before.author}")
            embed.add_embed_field(name="Message before", value=f"{message_before.content}")
            embed.add_embed_field(name="Message after", value=f"{message_after.content}")
            embed.add_embed_field(name="Guild", value=f"{message_before.guild.name}")
            embed.add_embed_field(name="Channel", value=f"{message_after.channel.mention}")
            webhook.add_embed(embed)
            response = webhook.execute()
        except:
            webhook = DiscordWebhook(
                url="WEBHOOK_HERE",
                rate_limit_retry=True)
            embed = DiscordEmbed(title='DM edited')
            embed.set_author(name=f"{message_before.author}")
            embed.add_embed_field(name="Message before", value=f"{message_before.content}")
            embed.add_embed_field(name="Message after", value=f"{message_after.content}")
            webhook.add_embed(embed)
            response = webhook.execute()
    else:
        ()
bot.run('DISCORD_TOKEN_HERE')
