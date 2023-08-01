import discord
import random
import json
from key import key
from random import choice

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
token = key.get("token")
# Idéias:
# 1- !tarefas | O bot fala as tarefas e trabalhos para entregar no momento. Acho vai ser meio difícil de fazer
# 2- !pontos {usuário} | O bot fala a quantia de pontos do usuário. Se eu soubesse como faz pra indentificar o usuário pela mensagem acho q dava pra fazer
# 3- !ips | O bot manda o IP do servidor do minecraft. Acho q esse é o menos provável q da certo de fazer pq depende de outros site
# 4- !help | O mais simples de fazer. O bot fala os comandos que ele tem
# 7- !cemitério | Arrumar a junção de dados dos servers e a melhorar


@client.event
async def on_ready():
    print(f"{client.user} está online!")


def escolher_usuario():
    usuarios_ativos = []
    for usuario in client.get_all_members():
        if not usuario.bot:  # and usuario.status == discord.enums.Status.online:
            usuarios_ativos.append(usuario.display_name)
    usuarios_ativos.extend(["Ninguém"] * 10)
    return choice(usuarios_ativos)


@client.event
async def on_message(message):
    conteudo = message.content
    conteudo_lower = conteudo.lower()

    if message.author == client.user:
        return

    if conteudo_lower.startswith("!online"):
        await message.channel.send("GP Bot está online!")

    elif conteudo_lower.startswith("!regras"):
        await message.channel.send(
            """As regras do serveridor são as seguinte: 
**1-** Você deve manter o "respeito", com os membros não ultrapassando os limites da zuera 
**2-** Você não pode spawmar mensagem para spawnar um pokémon em nenhum outro chat a não ser o Poke-chat
**3**- Você não pode mandar qualquer coisa que faça referencia a coisas obcenas
**4-** Você deve colocar áudios estorados em algum bot de música
**5-** Você não pode mandar nenhum vírus/malware na central de downloa
**6-** Caso esteje participando do GP Server, não desrespeitar as regras. Para saber quais são digite: !GP Server regras"""
        )

    elif conteudo_lower.startswith("!gp server regras"):
        await message.channel.send(
            """As regras do servidor do minecraft são as seguintes:
**1-**Proibido o uso de quaisquer armaduras do mod Project E, em caso de estar jogando em um modpack
**2-** Proibido o assassinato de qualquer pet de qualquer jogador
**3-** Proibido qualquer tipo de várzea contra qualquer estrutura oficial em alguma vila principal
**4-** Proibido usar recursos de outros jogadores sem consentimento ou trato
**5-** Qualquer residência ou estrutura que esteja dentro da vila que foi construída e não esteja dentro da temática da mesma corre o risco de ser destruída
**6-** Qualquer baú que não está próximo de uma residência ou estrutura pode ser roubado
**7-**Proibido qualquer dano a uma estrutura oficial ou a uma residência
**8-** Proibido usa qualquer comando para alterar o tempo do server"""
        )
    elif conteudo_lower.startswith("!d"):
        numero = int(conteudo_lower[2:])
        await message.channel.send(
            f":game_die: Caiu no **{random.randint(1, numero)}** :game_die:"
        )
    elif conteudo_lower.startswith("!cemitério"):
        await message.channel.send(
            f""":skull_crossbones: Quem morreu :skull_crossbones:: {escolher_usuario()}
:cry: Quem sofreu com a perda :cry:: {escolher_usuario()}
:partying_face: Quem comemorou a morte :partying_face:: {escolher_usuario()}
:detective: Investigou a morte :detective:: {escolher_usuario()}
:woman_detective: Ajudou a investigar :woman_detective:: {escolher_usuario()}
:knife: Quem matou :knife:: {escolher_usuario()}
:coffin: Esqueceu do velório :coffin:: {escolher_usuario()}
:health_worker: Ressuscitou o morto :health_worker:: {escolher_usuario()}
:man_zombie: Matou achando que era um zumbi :man_zombie:: {escolher_usuario()}"""
        )
    elif conteudo_lower.startswith("!tarefa"):
        with open(
            r"C:\Users\User\OneDrive\Programacao\aprender\discord_bot\tarefas.json", "r"
        ) as file:
            tarefas = json.load(file)
        await message.channel.send(f"{tarefas}")

    elif conteudo_lower.startswith("!help"):
        await message.channel.send(
            """Eu sou o GP Bot, fui feito com um primeiro projeto de progração do Mestre Giovani e vim das profundezas do SSD dele pra realizar algumas tarefas de forma automática, que são elas:
1- !d [algum número] | Nesse comando eu giro um dado com o total de lados do número escolhido e conto o resultado
2- !online | Esse comando é só pra saber se eu estou online mesmo
3- !regras | Nesse comando eu falo as regras do servidor
4- !!gp server regras | Nesse comando eu falo as regras do servidor do minecraft. Recomendado ver com frequência devido as mudanças frequêntes
5- !tarefas | Nesse comando eu mando as atuais (ou não) tarefas do 8 ano B
6- !cemitério | Nesse comando eu pego nome de jogadores aleatórios e simulo um velório (Idéia: Pareozitas)"""
        )


client.run(token)
