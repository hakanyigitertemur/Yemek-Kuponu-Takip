import asyncio
import discord
import time
import requests
from bs4 import BeautifulSoup
import random

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    son_kayitlar = []

    def kayit_control(a):
        if a not in son_kayitlar:
            son_kayitlar.append(a)
            return True
        else:
            return False

    point = 0

    print(f"Botunuz {client.user} adıyla giriş yaptı!")

    for guild in client.guilds:
        if guild.name == "SERVER NAME HERE": # sunucunuzun adini buraya yazin.
            break
    print(f'{client.user} sunucuda bulundu: {guild.name} (id: {guild.id})')

    kanal_adi = "gida-indirim" # botun hangi kanala mesaj atmak istediğini bu kanala yazın.

    kanal = discord.utils.get(guild.text_channels, name=kanal_adi)

    user = await client.fetch_user("USER ID HERE") # kendi kullanıcı id'niz.

    counter = 0

    if kanal is not None:
        while True:
            try:

                url = ["https://www.technopat.net/sosyal/bolum/indirim-koesesi.257/?prefix_id=30",
                       "https://forum.donanimarsivi.com/forumlar/Sicakfirsatlar"]
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0',
                           "Referer": "https://www.google.com/"}

                response = requests.get(url[point], headers=headers)

                yemek_adlari = ["getir", "Carrefoursa", "Yemeksepeti", "yemek", "Trendyol", "trendyol yemek", "Pizza",
                                "yemek sepeti", "Migros", "dominos", "domino's", "getiryemek", "Dondurma",
                                "getir kupon", "migros yemek"]

                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, "html.parser")
                    a_all = soup.find_all("a")
                    for i in a_all:
                        a_str = i.text
                        spliter = a_str.split()
                        for yemeks in yemek_adlari:
                            for split in spliter:
                                if yemeks.lower() == split.lower():
                                    if kayit_control(i.text):
                                        if point == 1:
                                            await kanal.send(
                                                f"**{i.text}**: https://forum.donanimarsivi.com{i['href']}")
                                            await user.send(f"**{i.text}**: https://forum.donanimarsivi.com{i['href']}")
                                        if point == 0:
                                            await kanal.send(
                                                f"**{i.text}**: https://www.technopat.net{i['href']}")
                                            await user.send(f"**{i.text}**: https://www.technopat.net{i['href']}")
                else:
                    print(response.status_code, response.reason)
                if point == 0:
                    point = point + 1
                else:
                    point = point - 1
                # time.sleep(random.randint(5, 7))
                await asyncio.sleep(random.randint(15, 25))

                await client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.listening,
                                              name=f"{counter} adet tarama yaptım."))
                counter = counter + 1

            except:
                print("Error occurred!")
    else:
        print("No channel found.")


client.run("BOT TOKEN HERE")