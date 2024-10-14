import discord


token = "Your token from Discord server"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
@client.event
async def on_message(message):
    if message.author == client.user:
        return

# This code is for poll vote in chat
    if message.content.startswith("!poll"):
        question = message.content[len("!poll "):].strip()
        if question:
            poll_message = await message.channel.send(f"Poll: {question}")
            await poll_message.add_reaction('❤️')
            await poll_message.add_reaction('❌')
        else:
            await message.channel.send("You didnt write question!")

# This code kick user if say LOL in chat
    if "LOL" in message.content:
        await message.channel.send("You cant say LOL")
        await message.author.kick(reason="You said LOL")

# This code respond with pong if you tipe ping in chat
    if message.content == "ping":
        await message.channel.send("pong")
client.run(token)