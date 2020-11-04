import discord
import os
import images

channel = os.getenv("CHANNELID")
id = 0
class MyClient(discord.Client):
    async def on_ready(self):
      print('Logged on as {0}!'.format(self.user))

    # async def on_message_delete(self, message):
    #   if str(message.content) == ' ' or message.author.bot == True or str(message.channel.id) != channel:
    #     pass
    #   else:
      
    #     global id

    #     images.construct_images(str(message.author), str(message.content), str(message.author.avatar_url), id, True)

    #     # print('Message from {0.author}: {0.content}'.format(message))

    #     id += 1

    async def on_message(self, message):
      
      if str(message.content) == ' ' or str(message.channel.id) != channel:
        pass
      else:
      
        global id

        images.construct_images(str(message.author), str(message.content), str(message.author.avatar_url), id)

        # print('Message from {0.author}: {0.content}'.format(message))

        id += 1

def start():
  client = MyClient() 
  client.run(os.getenv('BOT_TOKEN'))
