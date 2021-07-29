import discord
import asyncio
# Array list of people
people = [] * 0
groupnotification = "<@846942774241918996>" # Hard coded group ID that we use in our discord server

embedTF2Template = discord.Embed(
    title="Heads up Maggots!",
    description=("A Headcount for TF2 has been started, react with 👍 below to join."),
    color=discord.Color.orange()
)
embedFailTemplate = discord.Embed(
    title="Cancelled!",
    description="The caller cancelled the headcount.\nDeleting in 60 seconds...",
    color=discord.Color.red()
)
embedEndTemplate = discord.Embed(
    title="Fill The Rabbit Hole!",
    description="steam://connect/216.52.25.150:27015\nDeleting in 300 seconds...",
    color=discord.Color.green()
)
async def timer_deleteHeadCount(client,message,time):
    print("start")
    await asyncio.sleep(time)
    print("stop")
    await message.delete()

async def start_headcount(client, message):
    prog = await (message.channel).send(embed=embedTF2Template)
    await prog.add_reaction('👍')
    await prog.add_reaction('✅')
    await prog.add_reaction('❌')
    await message.delete()

async def update_headcount(client, reaction, user):
    if (user not in people):
        people.append(user)

    tempEmbed = embedTF2Template
    tempEmbed.clear_fields()

    if (reaction.count < 8):
        tempEmbed.add_field(name="Weak Status.", value=("{}/26 users have joined!").format(len(people)), inline=True)
    elif (reaction.count >= 8 and reaction.count < 12):
        tempEmbed.add_field(name="Good Status!", value=("{}/26 users have joined!").format(len(people)), inline=True)
    elif (reaction.count >= 12 and reaction.count < 16):
        tempEmbed.add_field(name="Great Status!", value=("{}/26 users have joined!").format(len(people)), inline=True)
    elif (reaction.count >= 16):
        tempEmbed.add_field(name="🎆WOAH MAMA!🎆", value=("{}/26 users have joined!").format(len(people)), inline=True)

    await reaction.message.edit(embed=embedTF2Template)

async def cancel_headcount(client, reaction, user):
    await reaction.message.edit(embed=embedFailTemplate)
    await asyncio.sleep(60)
    await reaction.message.delete()

async def end_headcount(client, reaction, user):
    await reaction.message.delete()
    tempEmbed = embedEndTemplate
    tempEmbed.add_field(name="Started!", value=("We got {} users!").format(len(people)))

    await reaction.message.channel.send(content=groupnotification, embed=embedEndTemplate)
    await asyncio.sleep(300)
    await reaction.message.delete()