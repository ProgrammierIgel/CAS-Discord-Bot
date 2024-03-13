import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('READY', self.user)

    async def on_message(self, message):
        print(f"{message.author}({message.channel}): {message.clean_content}")
        # don't respond to ourselves
        if message.author == self.user:
            return

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTIxNzUxNDY0NzMxODQyOTc3Ng.GhZxIC.u2IizstWsI5pJIM3kUJpu_aVFFlgDu9bDcs-eg')