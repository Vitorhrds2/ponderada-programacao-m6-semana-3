from animais import Animal
from recintos import Recinto

leao = Animal("Leão", "Felino", 50)
tigre = Animal("Tigre", "Felino", 60)
girafa = Animal("Girafa", "Herbívoro", 70)

recinto_felinos = Recinto("Recinto Felinos", "Felino")
recinto_herbivoros = Recinto("Recinto Herbívoros", "Herbívoro")

recinto_felinos.adicionar_animal(leao)
recinto_felinos.adicionar_animal(tigre)
recinto_herbivoros.adicionar_animal(girafa)

leao.alimentar()
tigre.alimentar()

visitantes_felinos = recinto_felinos.atrair_visitantes()
visitantes_herbivoros = recinto_herbivoros.atrair_visitantes()

print(f"{leao.nome} está com nível de felicidade {leao.nivel_felicidade}")
print(f"{tigre.nome} está com nível de felicidade {tigre.nivel_felicidade}")

print(f"O recinto de felinos atraiu {visitantes_felinos} visitantes.")
print(f"O recinto de herbívoros atraiu {visitantes_herbivoros} visitantes.")