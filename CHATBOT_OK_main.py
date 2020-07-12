from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import datetime

# ---- Inicio datetime ----
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
         'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'] #lista de meses para troca
hora = datetime.datetime.now()

a = hora.date()
lista = []
lista.append(a)
listastr = str(lista)

dia = listastr[24:26]
mes = listastr[21:22]
ano = listastr[15:19]

mesint = int(mes)

mes_palavra = meses[mesint]
z = dia, meses[mesint - 1],ano
resp_dia = z[0]
resp_hora = str(datetime.time(hora.hour, hora.minute, hora.second))
resp_mes = mesint
resp_ano = ano


bot = ChatBot('JULIUS: ')

conversa1 = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo!',
            'Você gosta de programar?', 'Sim', 'Qual linguagem você usa?', 'Eu programo em Python!',
            'Que legal', 'E você?']
conversa2 = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo!',
            'Você gosta de filmes?', 'Sim', 'Que tipo de filme?', 'Gosto de filmes de ação!',
            'Que legal', 'E você?']
conversa3 = ['Que horas são?', 'Agora são exatamente ' + resp_hora]
conversa4 = ['Que dia é hoje?', 'Hoje é dia ' + resp_dia]
conversa5 = ['Que mês estamos?', 'Estamos em ' + mes_palavra]
conversa6 = ['Que ano estamos?', 'Estamos em ' + resp_ano]

bot.set_trainer(ListTrainer)
bot.train(conversa1)
bot.train(conversa2)
bot.train(conversa3)
bot.train(conversa4)
bot.train(conversa5)
bot.train(conversa6)

while True:
    pergunta = input("Usuário:")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('JULIUS: ', resposta)
    else:
        print("JULIUS: Ainda não sei responder essa pergunta.")

