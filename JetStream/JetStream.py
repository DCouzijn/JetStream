import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run('MTEzODI5Nzg4MzMwMTUxMTE3OQ.Gv2z7g.jN39cdxMvUfRKGODEBfpap7HdbUsYQQjaObra4')
