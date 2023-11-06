class Recinto:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def atrair_visitantes(self):
        felicidade_total = sum(animal.nivel_felicidade for animal in self.animais)
        num_animais = len(self.animais)
        if num_animais > 0:
            felicidade_media = felicidade_total / num_animais
            return int(felicidade_media * num_animais)
        else:
            return 0
