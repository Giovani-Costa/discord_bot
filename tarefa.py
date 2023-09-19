import json


class Tarefa:
    def __init__(self, descricao: str, entrega: str) -> None:
        self.descricao = descricao
        self.entrega = entrega

    def reprentacao(self) -> str:
        return f"{self.descricao}  **{self.entrega}**"


class OrgananizadorDeTarefa:
    def __init__(
        self,
        atualizacao: str,
        artes: list[Tarefa],
        ciencias: list[Tarefa],
        historia: list[Tarefa],
        matematica: list[Tarefa],
        geografia: list[Tarefa],
        portugues: list[Tarefa],
        ingles: list[Tarefa],
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
    def from_json(cls, dados: dict) -> "OrganizadorDeTarefa":
        informacao = {
            materia: [Tarefa(**tarefa) for tarefa in tarefas]
            for materia, tarefas in dados.items()
            if materia != "atualizacao"
        }
        informacao["atualizacao"] = dados["atualizacao"]
        return cls(**informacao)

    def representacao(self) -> str:
        homework = f"""Última atualização: **{self.atualizacao}**

:art: Artes | **{len(self.artes)}**  {"  -  ".join([tarefa.reprentacao() for tarefa in self.artes])}
:test_tube: Ciências | **{len(self.ciencias)}**  {" - ".join([tarefa.reprentacao() for tarefa in self.ciencias])}
:books: História | **{len(self.historia)}**  {"  -  ".join([tarefa.reprentacao() for tarefa in self.historia])}
:abacus: Matemática | **{len(self.matematica)}**  {"  -  ".join([tarefa.reprentacao() for tarefa in self.matematica])} 
:earth_americas: Geografia | **{len(self.geografia)}**  {"  -  ".join([tarefa.reprentacao() for tarefa in self.geografia])}
:flag_br: Português | **{len(self.portugues)}**  {"  -  ".join([tarefa.reprentacao() for tarefa in self.portugues])}
:flag_us: Inglês | **{len(self.ingles)}**  {"  -  ".join([tarefa.reprentacao() for tarefa in self.ingles])}"""
        return homework
