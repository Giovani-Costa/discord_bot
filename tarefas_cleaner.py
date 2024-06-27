from datetime import date
import json

data_atual = date.today()
ano = data_atual.year

with open("tarefas.json", "r") as file:
    tarefas = json.load(file)
for k, v in tarefas.items():
    if k != "atualizacao":
        tarefas_a_fazer = []
        for tarefa in v:
            entrega = tarefa["entrega"]
            dia, mes = entrega.split("/")
            data = date(ano, int(mes), int(dia))
            if data > data_atual:
                tarefas_a_fazer.append(tarefa)
        tarefas[k] = tarefas_a_fazer
    else:
        tarefas[k] = f"{data_atual.day:02d}/{data_atual.month:02d}"
with open("tarefas.json", "w") as file:
    json.dump(tarefas, file, sort_keys=True, indent=4)
