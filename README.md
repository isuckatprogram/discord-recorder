### ????
This is a quick program that I created to easily record a discord chat on a video automatically. Made with [discord.py](https://discordpy.readthedocs.io/en/latest/). 

### Install Packages

You might need to run ``poetry install`` to install all the needed packages to run :3

### Setup

You will need one enviroment variables:

``
BOT_TOKEN
``

``
CHANNELID
``

- You need to create a discord application on the [developer portal](https://discord.com/developers/applications) and then create a bot and invite it to your server.
- Set the enviroment variable ``BOT_TOKEN`` to the token of the bot
- Create another enviroment variable called ``CHANNELID`` and set it to the channel you want the program to record
- Start the python program by running ``python3 main.py``
- Ask your friends to help you test it and send messages
- Once you are done, stop the program and you'll see a file called ``final.mp4`` in the directory
- Open that file and you'll see your discord chat on a video, created by a python program


### Important
If you don't have a computer with good storage, I don't recommend running this because this will generate an image for every message on your computer so if the program detect like ``120 messages`` there will be ``120 images`` on your computer generated for each message. To remove all the images run ``python3 reset.py``



### Coming Soon

- Ability to record this live to youtube so you can basically live stream it to a youtube video