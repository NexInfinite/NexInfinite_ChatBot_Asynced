#install (look at README for help)
from config import *
import asyncio
from asynctwitch import *

#starter message
class TwitchBot(CommandBot):
    async def _join(self, channel):
        await super()._join(channel),
        await say('Im here now, ok? Streamer, are you ok with that?')
        await bot._send_privmsg('nex_infinite', '/color SpringGreen')

#defining the msg output using async
async def say(msg):
    await bot.say(channel_name, msg)

#defining the async loops
async def delay_say(msg, delay):
    await asyncio.sleep(delay)
    await say(msg)

#main loop
if __name__ == '__main__':
    bot = TwitchBot(user=nickname, channel=channel_name, oauth=oauth, prefix='') #gets the tokens from 'config'

    #Hi command (use this example to make more
    @bot.command('hi')
    async def hi(msg, *args):
        await say(f'Hello person, your name seems to be @{msg.author.name}, correct? Welcome erm.... Person?')

########################################################################################################################
                        #This will be where you put your commands (these are mine so far)
########################################################################################################################

    @bot.command('userman')
    async def userman(msg):
        await say(f'Userman??? More like HelperMan <3')

    @bot.command('ur')
    async def ur(msg):
        await say(f'No u')

    @bot.command('red')
    async def bot_colour_red(msg):
        await bot._send_privmsg('nex_infinite', '/color Red')
        await say(f'Bot colour is now red')

    @bot.command('green')
    async def bot_colour_green(msg):
        await bot._send_privmsg('nex_infinite', '/color Green')
        await say(f'Bot colour is now green')

    @bot.command('blue')
    async def bot_colour_blue(msg):
        await bot._send_privmsg('nex_infinite', '/color Blue')
        await say(f'Bot colour is now Blue')

    @bot.command('default')
    async def bot_colour_defualt(msg):
        await bot._send_privmsg('nex_infinite', '/color SpringGreen')
        await say(f'Bot colour is now Default (SpringGreen)')

    @bot.command('mods')
    async def who_are_the_mods(msg):
        await say(f'The mods are')
        await asyncio.sleep(0.5)
        await say(f'andrewgamer1937, comsciprogramming, gabelover23, gconnor911, hexploitation, malvious_mh, nex_infinite, nezamizero, nightbot, streamelements, sudokid, userman2, wizebot, yojimbozz, learngamedev')

    @bot.command('age')
    async def how_old_are_you(msg):
        await say(f'I am 14, get on my level (its button 3 btw) Kappa')

    @bot.command('rainbow123')
    async def chat_colour_rainbow(msg):
        await say(f'There WILL be a 8 seconde delay between msg for the rainbow effect to work, sorry its how it works :(')
        await bot._send_privmsg('nex_infinite', '/color Red')
        await asyncio.sleep(0.3)
        await say(f'<')
        await asyncio.sleep(6)
        await bot._send_privmsg('nex_infinite', '/color Orange Red')
        await asyncio.sleep(0.3)
        await say(f'<')
        await asyncio.sleep(6)
        await bot._send_privmsg('nex_infinite', '/color Goldenrod')
        await asyncio.sleep(0.3)
        await say(f'<')
        await asyncio.sleep(6)
        await bot._send_privmsg('nex_infinite', '/color Green')
        await asyncio.sleep(0.3)
        await say(f'<')
        await asyncio.sleep(6)
        await bot._send_privmsg('nex_infinite', '/color Dodger Blue')
        await asyncio.sleep(0.3)
        await say(f'<')
        await asyncio.sleep(6)
        await bot._send_privmsg('nex_infinite', '/color Blue')
        await asyncio.sleep(0.3)
        await say(f'<')
        await asyncio.sleep(4)
        await bot._send_privmsg('nex_infinite', '/color Blue Violet')
        await asyncio.sleep(0.3)
        await say(f'<')
        await asyncio.sleep(6)


########################################################################################################################
                                        #where you define the loop commands
########################################################################################################################

    @bot.override
    async def event_message(m):
        print(m)
        await bot.parse_commands(m)

    async def Welcome_loop():
        while True:
            await asyncio.sleep(120)
            await say('Welcome everyone, If you are new and enjoy the stream hit follow to keep up!')

    async def Viewer_loop():
        while True:
            await asyncio.sleep(2)
            print(f'The viewer count is {bot.viewer_count["#nex_infinite"]}')

    #where you initialize the loop commands

    #asyncio.ensure_future(Welcome_loop())
    #asyncio.ensure_future(Viewer_loop())
    bot.start()
