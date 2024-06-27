from datetime import date
import json

data_atual = date.today()
ano = data_atual.year

with open("provas.json", "r") as file:
    provas = json.load(file)
for k, prova in provas.items():
    if k != "atualizacao":
        if prova is not None:
            entrega = prova["data"]
            dia, mes = entrega.split("/")
            data = date(ano, int(mes), int(dia))
            if data < data_atual:
                provas[k] = None
    else:
        provas[k] = f"{data_atual.day:02d}/{data_atual.month:02d}"
with open("provas.json", "w") as file:
    json.dump(provas, file, sort_keys=True, indent=4)
