"""
Created on Wed Dec 30 23:53:34 2020

@author: Martim
"""

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='')
lista=['f�cil', 'facil', 'Facil']    

@client.event
async def on_message(msg):
    contents=msg.content.split(' ')   
    for word in contents:            
        if word == 'facil' or word == 'f�cil' or word == 'Facil':
            await msg.channel.send('F�cil tipo eu')
        if word == 'daltonico':
            await msg.channel.send('Olha a� isso � bu� mau')
        if word == 'noice' or word == 'nice':
            await msg.channel.send('O martim(daddy) � bu� cool por acaso')
        if word == 'noob':
            await msg.channel.send('O meu daddy programou-me para dizer que o miguel � alta noobalh�o mas o ruben at� joga fixe, altough ningu�m supera el fant�stico silver surfer do rocket')
        if word == 'bruno':
            await msg.channel.send('N�o entendi, tentou dizer Ruben?')
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
        await msg.channel.send('correr atr�s')
    if "im depressed" in msg.content:
        await msg.channel.send("Hi depressed i'm... CALA A BOCA DAD BOT DA PI�A")
    if 'eutounafesta' in msg.content:
        await msg.channel.send("Eu tou na festa\nNa festa\nEu tou na festa\nEu tou no mini\nEu tou na festa\nEuEu tou na\n(Eu nem sei onde 'tou)\nEu tou na moca, tou com coca\nAo p� de mim tenho ganda porca\nNem conhe�o n�o importa\nSentimento badalhoca\nTou na moca tou com tilha\nV�rias putas na breguilha\nTanta coca, juiz de linha\nTenho tudo na bolsinha\nN�s nem pagamos o beat\nQue safoda, j� caguei\nSempre que disparo � em gajos\nPorque a minha Glock � gay\nGlock � puta, Glock � vaca\nTou na festa e trouxe a placa\nJ� nem sinto a ressaca\nPuta que pariu a b�fia\� pala da walkie-talkie\nEu conhe�o a tua dama\nEla tem um ganda ass\nMas eu ando sempre blessed\nEu tou na festa\nEu tou no mini\nEu tou na festa\nEu tou na festa\nEu tou na\nEu tou na\n(Eu nem sei onde 'tou)\nEu tenho Whisky no meu bongo\nE Abri-lhe a testa, levou pontos\nCom essas putas n�o converso\nGandas touras 't�o com o cio\nSe � para falar do cash\nSe for menos de 100 n�o negocio\nEu tou na merda c'os rapazes\nMas eu 'tou fixe n�o vacilo\nFalam mal das minhas porcas\nPorque n�o peram com quem tchilo\nTenho bitches no meu copo\nEu j� nem sei 'tou todo cego\nSabes que eu caguei p'ros cops\nEu tou pregado tipo um prego\nEu n�o sou dos Dealema\nMas 'tou no segundo piso\nE a tua dama � uma kenga\nSabes que mamou no pi�o\n� o que � mano � lidar\nSe eu tou na festa � pra dan�ar\nRest in peace, Jo�o Santos\nA gaja do ano\nEu tou na festa\nEu tou no mini\nEu tou na festa\nEu tou na festa\nEu tou na\nEu tou na\n(Eu nem sei onde 'tou)\nTu pagas uber � tua Sheila\nPra ela vir levar de 4\nBoy tas sempre a mandar text\nTu �s mesmo um ganda chato\nEuDessa merda eu j� tou farto\nQuero foder uma chinesa\nJe esta fuck com uma avec\nEu n�o entendo o teu parlapier\nSe n�o sabes o meu nome\nCara podre eu sou o Z�\nTanta merda no meu corpo\nSe n�o sabes o meu nome\nGanda ot�rio eu sou o Z�\nGanda ot�rio n�o d�s leak\nPorque isso � po nosso EP\nEu sou a For�a Suprema\nOs Kalema, e o T�p�\nEu tou a perar uma beta\nEla me chama de voc�\nEu tou mesmo todo cego\nE nem sequer sei porque\n")

client.run('NzkzOTg5Mjg0MjU5OTU0NzU5.X-0SJA.0PMbi8Oey0bxSghFY92w1hcKDDI')