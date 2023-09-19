import json


class Prova:
    def __init__(self, resumo: str, data: str) -> None:
        self.resumo = resumo
        self.data = data


class OrgananizadorDeProvas:
    def __init__(
        self,
        atualizacao: str,
        artes: Prova,
        ciencias: Prova,
        historia: Prova,
        matematica: Prova,
        geografia: Prova,
        portugues: Prova,
        ingles: Prova,
    ) -> None:
        self.atualizacao = atualizacao
        self.artes = artes
        self.ciencias = ciencias
        self.historia = historia
        self.matematica = matematica
        self.geografia = geografia
        self.portugues = portugues
        self.ingles = ingles

    @classmethod
    def from_json(cls, dados: dict) -> "OrganizadorDeProvas":
        informacao = {}
        for materia, prova in dados.items():
            if prova:
                if materia == "atualizacao":
                    informacao[materia] = prova
                else:
                    informacao[materia] = Prova(**prova)
            else:
                informacao[materia] = Prova("", "")
        return cls(**informacao)

    def representacao(self) -> str:
        exams = f"""Última atualização: **{self.atualizacao}**

:art: Artes |  {self.artes.data}
:test_tube: Ciências | {self.ciencias.data}
:books: História | {self.historia.data}
:abacus: Matemática | {self.matematica.data} 
:earth_americas: Geografia | {self.geografia.data}
:flag_br: Português | {self.portugues.data}
:flag_us: Inglês | {self.ingles.data}"""
        return exams

    def representacao_resumo(self, materia: str) -> str:
        try:
            prova: Prova
            prova = getattr(self, materia)
            return prova.resumo
        except AttributeError:
            return f"{materia} não existe"
