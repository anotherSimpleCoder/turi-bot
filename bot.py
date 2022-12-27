from Lexer import Lexer
from Parser import Parser
from Evaluator import Evaluator

import discord
import sys

import wave
import subprocess

FULL_LYRICS = 'Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha Turi ip ip ip Ip ip ip ip tsha ik Ip tura ip ik Eugh eugh isha ik turisha'

devmode = False
logmode = False

DEV_TOKEN = '<token>'


def run_bot():
    TOKEN = '<token>'
    client = discord.Bot(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')


    @client.command(description="Generates turi-ip sound")
    async def generate(ctx, input):
        user = str(ctx.author)
        channel = str(ctx.channel)

        if logmode:
            print(f'{user} sent {input} in {channel}')

        if 'turi-bot' in channel:
            if devmode:
                if user != 'ampir3#8697':
                    await ctx.respond(f'This bot is currently under maintenance :/')
                    return


            if input == FULL_LYRICS:
                await ctx.respond(f'🤔')
                await ctx.channel.send(file=discord.File(r'poopies.mp3'))

            else:
                if 'turi' in input or 'ip' in input:
                    await ctx.respond(f'generating sound...')
                    compile_sound(input, False, 0)
                    await ctx.delete()
                    await ctx.channel.send(f'{input}')
                    await ctx.channel.send(file=discord.File(r'res.mp3'))

                else:
                    await ctx.respond(f"Sorry I can't understand what you're saying :/")

    @client.command(description="help lol")
    async def help(ctx):
        user = str(ctx.author)
        channel = str(ctx.channel)

        if logmode:
            print(f'{user} asked for help in {channel}')

        if 'turi-bot' in channel:
            if devmode:
                if user != 'ampir3#8697':
                    await ctx.respond(f'This bot is currently under maintenance :/')
                    return

            await ctx.respond(f'check your dms!')
            await ctx.author.send('''
                In order to generate your turi ip sound, just type in
                /generate <sequence of turi and ip's>

                /slowdown <sequence of turi and ip's>
                
                In case you are an admin who added this bot to the server:
                turi-bot only works in a channel called #turi-bot
                
                /help sends you this DM for help''')

    @client.command(description='slowed down turi-ip')
    async def slowdown(ctx, input, slow_factor):
        slow_factor = float(slow_factor)

        if slow_factor > 1:
            await ctx.respond(f'Your slowdown factor is too high. It needs to be between 0.1 - 1')
            return

        user = str(ctx.author)
        channel = str(ctx.channel)

        if logmode:
            print(f'{user} sent {input} in {channel}')

        if 'turi-bot' in channel:
            if devmode:
                if user != 'ampir3#8697':
                    await ctx.respond(f'This bot is currently under maintenance :/')
                    return


            if input == FULL_LYRICS:
                await ctx.respond(f'🤔')
                await ctx.channel.send(file=discord.File(r'slow_poopies.mp3'))

            else:
                if 'turi' in input or 'ip' in input:
                    await ctx.respond(f'generating sound...')
                    compile_sound(input, True, slow_factor)
                    await ctx.delete()
                    await ctx.channel.send(f'{input} (slowed)')
                    await ctx.channel.send(file=discord.File(r'res.mp3'))

                else:
                    await ctx.respond(f"Sorry I can't understand what you're saying :/")


    @client.command(description='sped-up turi-ip')
    async def speedup(ctx, input, speed_factor):
        speed_factor = float(speed_factor)

        if speed_factor <= 1:
            await ctx.respond(f'Your slowdown factor is too low. It needs to be above 1')
            return

        user = str(ctx.author)
        channel = str(ctx.channel)

        if logmode:
            print(f'{user} sent {input} in {channel}')

        if 'turi-bot' in channel:
            if devmode:
                if user != 'ampir3#8697':
                    await ctx.respond(f'This bot is currently under maintenance :/')
                    return


            if input == FULL_LYRICS:
                await ctx.respond(f'🤔')
                await ctx.channel.send(file=discord.File(r'quick_poopies.mp3'))

            else:
                if 'turi' in input or 'ip' in input:
                    await ctx.respond(f'generating sound...')
                    compile_sound(input, True, speed_factor)
                    await ctx.delete()
                    await ctx.channel.send(f'{input} (speed-up)')
                    await ctx.channel.send(file=discord.File(r'res.mp3'))

                else:
                    await ctx.respond(f"Sorry I can't understand what you're saying :/")
        


    if devmode:
        client.run(DEV_TOKEN)

    else:
        client.run(TOKEN)






def compile_sound(test_input, speed_change, factor):
    #test_input = '''turi turi turi'''
    l = Lexer()

    t_list = l.lex(test_input)
    p = Parser(t_list)
    w_list = p.parse()

    e = Evaluator(w_list)
    e.eval()
    e.combine_clips('res.mp3')

    if speed_change:
        slowing('res.mp3', factor)

def slowing(filename, slow_factor):
    subprocess.run(['ffmpeg', '-i', filename, 'slow.wav'])
    spf = wave.open('slow.wav', 'rb')
    signal = spf.readframes(-1)

    wf = wave.open('slowed.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(spf.getframerate() * slow_factor)
    wf.writeframes(signal)
    wf.close()

    subprocess.run(['rm', '-r','slow.wav'])
    subprocess.run(['rm', '-r', filename])
    subprocess.run(['ffmpeg', '-i', 'slowed.wav', filename])
    subprocess.run(['rm', '-r', 'slowed.wav'])
    

if __name__ == "__main__":
    print(len(sys.argv))

    if len(sys.argv) > 1:
        if sys.argv[1] == 'dev-mode':
            print('devmode activated!')
            devmode = True

        elif sys.argv[1] == 'log-mode':
            print('logmode activated!')
            logmode = True


    run_bot()
