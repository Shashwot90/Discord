# This example requires the 'message_content' intent.
#1261537084221427724
#00c1d00f429c098d3ec116c3ab0123511d1132ad82b6d385be084a934dad4163
import discord
import os
import openai 

 
openai.api_key = os.getenv("OPENAI_API_KEY")


token = os.getenv("SECRET_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(message.mentions)
        if self.user != message.author:
            if self.user in message.mentions:
                channel = message.channel
                response = openai.Completion.create(
                  model="gpt-3.5-turbo-16k",
                  prompt=message.content,
                  temperature=1,
                  max_tokens=256,
                  top_p=1,
                  frequency_penalty=0,
                  presence_penalty=0
                )
                messageToSend = response.choices[0].text
                await channel.send(messageToSend)
         

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)

