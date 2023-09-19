import discord
import random
import json
from unidecode import unidecode
from key import key
from random import choice
from tarefa import OrgananizadorDeTarefa
from provas import OrgananizadorDeProvas

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
token = key.get("token")
# Idéias:
# 1- !pontos {usuário} | Dar uma otimizada
# 2- !ips | O bot manda o IP do servidor do minecraft. Acho q esse é o menos provável q da certo de fazer pq depende de outros site
# 3- !help | Atualizar o help
# 4- !tarefa | Script de limpeza
# 5- !prova | Script de limpeza


@client.event
async def on_ready():
    print(f"{client.user} está online!")


def escolher_usuario():
    usuarios_ativos = [
        usuario.display_name for usuario in client.get_all_members() if not usuario.bot
    ]
    return choice(usuarios_ativos)


def escolher_para_cemiterio():
    probabilidade = random.randint(1, 100)
    if probabilidade <= 15:
        return "Ninguém"
    else:
        return escolher_usuario()


@client.event
async def on_message(message):
    autor_da_mensagem = message.author
    autor_da_mensagem = str(autor_da_mensagem)
    display_name_do_autor_da_mensagem = message.author.display_name
    conteudo = message.content
    conteudo_lower = unidecode(conteudo.lower())

    if message.author == client.user:
        return

    if conteudo_lower.startswith("!online"):
        await message.channel.send("GP Bot está online!")

    elif conteudo_lower.startswith("!regras"):
        await message.channel.send(
            """As regras do serveridor são as seguinte: 
**1-** Você deve manter o "respeito", com os membros não ultrapassando os limites da zuera
**2-** Você não pode spawmar mensagem para spawnar um pokémon em nenhum outro chat a não ser o Poke-chat
**3-** Você não pode mandar qualquer coisa que faça referencia a coisas obcenas
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
    elif conteudo_lower.startswith("!cemiterio"):
        await message.channel.send(
            f""":skull_crossbones: Quem morreu :skull_crossbones:: {escolher_para_cemiterio()}
:cry: Quem sofreu com a perda :cry:: {escolher_para_cemiterio()}
:partying_face: Quem comemorou a morte :partying_face:: {escolher_para_cemiterio()}
:detective: Investigou a morte :detective:: {escolher_para_cemiterio()}
:woman_detective: Ajudou a investigar :woman_detective:: {escolher_para_cemiterio()}
:knife: Quem matou :knife:: {escolher_para_cemiterio()}
:coffin: Esqueceu do velório :coffin:: {escolher_para_cemiterio()}
:health_worker: Ressuscitou o morto :health_worker:: {escolher_para_cemiterio()}
:man_zombie: Matou achando que era um zumbi :man_zombie:: {escolher_para_cemiterio()}"""
        )
    elif conteudo_lower.startswith("!tarefa"):
        with open(
            r"C:\Users\User\OneDrive\Programacao\discord_bot\tarefas.json", "r"
        ) as file:
            tarefas = json.load(file)
        organizador_de_prova = OrgananizadorDeTarefa.from_json(tarefas)
        await message.channel.send(organizador_de_prova.representacao())

    elif conteudo_lower.startswith("!help"):
        await message.channel.send(
            """Eu sou o GP Bot, fui feito com um primeiro projeto de progração do Mestre Giovani e vim das profundezas do SSD dele pra realizar algumas tarefas de forma automática, que são elas:
:game_die:  **1-** !d [algum número] | Nesse comando eu giro um dado com o total de lados do número escolhido e conto o resultado  :game_die:
:zap:  **2-** !online | Esse comando é só pra saber se eu estou online mesmo  :zap:
:clipboard:  **3-** !regras | Nesse comando eu falo as regras do servidor  :clipboard:
:pencil:  **4-** !!gp server regras | Nesse comando eu falo as regras do servidor do minecraft. Recomendado ver com frequência devido as mudanças frequêntes  :pencil:
:books:  **5-** !tarefas | Nesse comando eu mando as atuais (ou não) tarefas do 8 ano B  :books:
:coffin:  **6-** !cemitério | Nesse comando eu pego nome de jogadores aleatórios e simulo um velório (Idéia: Pareozitas)  :coffin:
:gp_point: **7-** !pontos | Nesse comando eu digo a sua quantidade de pontos  :gp_point:"""
        )

    elif conteudo_lower.startswith("!pontos"):
        with open(
            r"C:\Users\User\OneDrive\Programacao\discord_bot\pontos.json", "r"
        ) as file:
            pontos = json.load(file)
        points = {p["nome"]: p["pontos"] for p in pontos}
        argumentos = conteudo_lower.split()
        operadores = ["yodah_"]
        if len(argumentos) == 1:
            if autor_da_mensagem in points:
                await message.channel.send(
                    f"{display_name_do_autor_da_mensagem} tem {points[autor_da_mensagem]} pontos!"
                )

            else:
                await message.channel.send("Você não consta no meu banco de dados!")
        elif autor_da_mensagem in operadores:
            if len(argumentos) == 4:
                if argumentos[1] == "add":
                    if argumentos[2] in points:
                        points[argumentos[2]] += int(argumentos[3])
                        with open(
                            r"C:\Users\User\OneDrive\Programacao\discord_bot\pontos.json",
                            "w",
                        ) as file:
                            json.dump(
                                [{"nome": k, "pontos": v} for k, v in points.items()],
                                file,
                                indent=4,
                            )
                        await message.channel.send("Operação realizada")
                    else:
                        await message.channel.send(
                            f"{argumentos[2]} não consta no meu banco de dados!"
                        )
                elif argumentos[1] == "rem":
                    if argumentos[2] in points:
                        points[argumentos[2]] -= int(argumentos[3])
                        with open(
                            r"C:\Users\User\OneDrive\Programacao\discord_bot\pontos.json",
                            "w",
                        ) as file:
                            json.dump(
                                [{"nome": k, "pontos": v} for k, v in points.items()],
                                file,
                                indent=4,
                            )
                        await message.channel.send("Operação realizada")
                    else:
                        await message.channel.send(
                            f"{argumentos[2]} não consta no meu banco de dados!"
                        )
                else:
                    await message.channel.send(
                        "Algo de errado não está certo, tente conferir se a operação está correta"
                    )
            else:
                await message.channel.send(
                    "Algo de errado não está certo, tente reescrever o comando"
                )
        else:
            await message.channel.send(
                "Você não tem permissão para realizar esse comando"
            )

    elif conteudo_lower.startswith("!ticket"):
        ticket_chat = client.get_channel(1148760030099804242)
        await ticket_chat.send("teste")

    elif conteudo_lower.startswith("!ship"):
        usuario_1 = escolher_usuario()
        usuario_2 = escolher_usuario()
        ship = usuario_1[0 : len(usuario_1) // 2] + usuario_2[len(usuario_2) // 2 :]
        porcentagem = random.randint(1, 100)
        await message.channel.send(
            f""":hearts:  Hmm, que bunitinhuuu  :hearts:
{usuario_1}  +  {usuario_2} =  :sparkles:  **{ship}  {porcentagem}%  :sparkles:**"""
        )
    elif conteudo_lower.startswith("!prova"):
        with open(
            r"C:\Users\User\OneDrive\Programacao\discord_bot\provas.json", "r"
        ) as file:
            tarefas = json.load(file)
        organizador_de_prova = OrgananizadorDeProvas.from_json(tarefas)
        argumentos = conteudo_lower.split()
        if len(argumentos) == 1:
            await message.channel.send(organizador_de_prova.representacao())
        else:
            await message.channel.send(
                organizador_de_prova.representacao_resumo(argumentos[1])
            )


client.run(token)
