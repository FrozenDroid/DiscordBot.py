#!/usr/bin/python3
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)

client.run('');
