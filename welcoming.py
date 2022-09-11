import discord
from attr import __description__
import discord, datetime
from discord import client
from datetime import datetime
from discord.ext.commands import bot
from os import system
from webserver import keep_alive
import os

#bot= bot("!")
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
ROLE = 'Anak Baru'


#Discord Status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing, name='Kelas Terbuka'))


#Welcoming
@client.event
async def on_member_join(member):
    guild = client.get_guild(882540885714305064)
    welcome_channel = guild.get_channel(1005001820449538098)
    em = discord.Embed(
        title=f"Hai,{member.name}! ",
        color=discord.Color.random(),
        timestamp=datetime.utcnow()
    ).add_field(
        name=f"Selamat datang di server Discord {guild.name} ^^ ",
        value=
        f"""**1. Sebelum kamu menjelajahi server discord ini,** silahkan cek terlebih dahulu **Rules** yang ada di <#882882991175659550> 
        
        **2. Setelah kamu mengecek Rules, silahkan** perkenalkan dirimu di <#1004023967192977566> agar kamu mendapatkan role <@&1004013086497316914> dan mendapatkan akses channel lainnya.

        **3. Setelah kamu melakukan perkenalan, silahkan** **claim role** di <#1006404658551607336> dengan memberi react pesan yang tersedia untuk mengakses channel tambahan (dapat dipilih lebih dari 1).

        4. Apabila ada **permasalahan** yang ingin dipertanyakan, silahkan **hubungi** <@&884816238344282132>. Keep coding stay Awesome! ^^
        """).set_footer(text=f"Discord.py")
    em.set_thumbnail(url=member.avatar_url)
    #profile= Editor(profile_image).resize((150,150)).circle_image()
    em.set_image(
        url=
        "https://cdn.discordapp.com/attachments/882540885714305067/1005424054930505759/banner_discord-01.png"
    )

    await welcome_channel.send(
        f"Tes-Tes, dengan{member.mention} disini? :wave:", embed=em)
    await member.send(
        f'Kamu baru saja bergabung di server Discord {guild.name}, {member.name}. Buat dirimu senyaman mungkin ya ^^  :partying_face:'
    )


@client.event
async def on_member_remove(member):
    print(f"{member} has left!")
    leave_channel = client.get_channel(1005001820449538098)
    await leave_channel.send(
        f"{member.mention} telah meninggalkan server, sampai jumpa~ :wave:")

    try:
        await member.send(f"Hey {member.display_name}! sampai jumpa~ :wave:")
    except:
        await leave_channel.send(f"{member.mention} , Adios :wave:")


#<#954191378143911947>


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1006420237614325782:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'cpp':
            role = discord.utils.get(guild.roles, name='C++')
        elif payload.emoji.name == 'clang':
            role = discord.utils.get(guild.roles, name='C')
        elif payload.emoji.name == 'csharp':
            role = discord.utils.get(guild.roles, name='C#')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id,
                                        guild.members)
            if member is not None:
                await member.add_roles(role)
                print("Telah Ditambahkan")
            else:
                print("Member tidak ditemukan")
        else:
            print("Role tidak ditemukan")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 1006420237614325782:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'cpp':
            role = discord.utils.get(guild.roles, name='C++')
        elif payload.emoji.name == 'clang':
            role = discord.utils.get(guild.roles, name='C')
        elif payload.emoji.name == 'csharp':
            role = discord.utils.get(guild.roles, name='C#')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id,
                                        guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("Telah Ditambahkan")
            else:
                print("Member tidak ditemukan")
        else:
            print("Role tidak ditemukan")


keep_alive()
try:
    TOKEN = os.environ.get("DISCORD_BOT_SECRET")
    client.run(TOKEN)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system("restarter.py")
    system('kill 1')
