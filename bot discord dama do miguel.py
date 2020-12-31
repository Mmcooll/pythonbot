"""
Created on Wed Dec 30 23:53:34 2020

@author: Martim
"""

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='')
lista=['fácil', 'facil', 'Facil']    

@client.event
async def on_message(msg):
    contents=msg.content.split(' ')   
    for word in contents:            
        if word == 'facil' or word == 'fácil' or word == 'Facil':
            await msg.channel.send('Fácil tipo eu')
        if word == 'daltonico':
            await msg.channel.send('Olha aí isso é bué mau')
        if word == 'noice' or word == 'nice':
            await msg.channel.send('O martim(daddy) é bué cool por acaso')
        if word == 'noob':
            await msg.channel.send('O meu daddy programou-me para dizer que o miguel é alta noobalhão mas o ruben até joga fixe, altough ninguém supera el fantástico silver surfer do rocket')
        if word == 'bruno':
            await msg.channel.send('Não entendi, tentou dizer Ruben?')
        if word == 'desculpa':
            for i in range(10):
                await msg.channel.send('sorry')
            
            
    if 'gay' in msg.content:
        await msg.channel.send('haha mesmo')
    if 'how could you leave us' in msg.content:
        await msg.channel.send('!play my mom is dead')
    if 'this is the life' in msg.content:
        await msg.channel.send('IN AMADORAAAA')
    if 'andas na street' in msg.content:
        await msg.channel.send('DE METRALHADORAAAAAAAAAAA')
    if 'ima ima ima' in msg.content:
        await msg.channel.send('correr atrás')
    if "im depressed" in msg.content:
        await msg.channel.send("Hi depressed i'm... CALA A BOCA DAD BOT DA PIÇA")
    if 'eutounafesta' in msg.content:
        await msg.channel.send("Eu tou na festa\nNa festa\nEu tou na festa\nEu tou no mini\nEu tou na festa\nEuEu tou na\n(Eu nem sei onde 'tou)\nEu tou na moca, tou com coca\nAo pé de mim tenho ganda porca\nNem conheço não importa\nSentimento badalhoca\nTou na moca tou com tilha\nVárias putas na breguilha\nTanta coca, juiz de linha\nTenho tudo na bolsinha\nNós nem pagamos o beat\nQue safoda, já caguei\nSempre que disparo é em gajos\nPorque a minha Glock é gay\nGlock é puta, Glock é vaca\nTou na festa e trouxe a placa\nJá nem sinto a ressaca\nPuta que pariu a bófia\À pala da walkie-talkie\nEu conheço a tua dama\nEla tem um ganda ass\nMas eu ando sempre blessed\nEu tou na festa\nEu tou no mini\nEu tou na festa\nEu tou na festa\nEu tou na\nEu tou na\n(Eu nem sei onde 'tou)\nEu tenho Whisky no meu bongo\nE Abri-lhe a testa, levou pontos\nCom essas putas não converso\nGandas touras 'tão com o cio\nSe é para falar do cash\nSe for menos de 100 não negocio\nEu tou na merda c'os rapazes\nMas eu 'tou fixe não vacilo\nFalam mal das minhas porcas\nPorque não peram com quem tchilo\nTenho bitches no meu copo\nEu já nem sei 'tou todo cego\nSabes que eu caguei p'ros cops\nEu tou pregado tipo um prego\nEu não sou dos Dealema\nMas 'tou no segundo piso\nE a tua dama é uma kenga\nSabes que mamou no piço\nÉ o que é mano é lidar\nSe eu tou na festa é pra dançar\nRest in peace, João Santos\nA gaja do ano\nEu tou na festa\nEu tou no mini\nEu tou na festa\nEu tou na festa\nEu tou na\nEu tou na\n(Eu nem sei onde 'tou)\nTu pagas uber à tua Sheila\nPra ela vir levar de 4\nBoy tas sempre a mandar text\nTu és mesmo um ganda chato\nEuDessa merda eu já tou farto\nQuero foder uma chinesa\nJe esta fuck com uma avec\nEu não entendo o teu parlapier\nSe não sabes o meu nome\nCara podre eu sou o Zé\nTanta merda no meu corpo\nSe não sabes o meu nome\nGanda otário eu sou o Zé\nGanda otário não dês leak\nPorque isso é po nosso EP\nEu sou a Força Suprema\nOs Kalema, e o Tópê\nEu tou a perar uma beta\nEla me chama de você\nEu tou mesmo todo cego\nE nem sequer sei porque\n")

client.run('NzkzOTg5Mjg0MjU5OTU0NzU5.X-0SJA.0PMbi8Oey0bxSghFY92w1hcKDDI')