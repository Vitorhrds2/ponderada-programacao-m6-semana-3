class Animal:
    def __init__(self, nome, especie, nivel_felicidade):
        self.nome = nome
        self.especie = especie
        self.nivel_felicidade = nivel_felicidade

    def alimentar(self):
        self.nivel_felicidade += 10