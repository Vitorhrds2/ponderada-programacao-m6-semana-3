# Relatório - API para Zoológico

Neste relatório, descreverei a estrutura do código para uma API de zoológico e os testes unitários associados a ela. A API permite criar animais, recintos, alimentar animais e atrair visitantes para o zoológico.

## Classes

### `Animal`
A classe `Animal` representa um animal no zoológico com as seguintes propriedades:
- `nome`: Nome do animal.
- `especie`: Espécie do animal.
- `nivel_felicidade`: Nível de felicidade do animal.

Além disso, a classe possui um método `alimentar` que aumenta o nível de felicidade do animal em 10.

### `Recinto`
A classe `Recinto` representa um recinto no zoológico com as seguintes propriedades:
- `nome`: Nome do recinto.
- `especie`: Espécie predominante no recinto.
- `animais`: Lista de animais no recinto.

A classe possui um método `adicionar_animal` para adicionar animais ao recinto e um método `atrair_visitantes` que calcula o número de visitantes atraídos com base na felicidade média dos animais no recinto.

## Exemplo de Uso

```python
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
```

## Testes Unitários

### Teste da classe `Animal`

```python
import unittest
from animais import Animal

class TestAnimal(unittest.TestCase):
    def test_alimentar(self):
        animal = Animal("Leão", "Felino", 50)
        animal.alimentar()
        self.assertEqual(animal.nivel_felicidade, 60)

if __name__ == '__main__':
    unittest.main()
```

Este teste verifica se o método `alimentar` da classe `Animal` funciona corretamente ao aumentar o nível de felicidade em 10.

### Teste da classe `Recinto`

```python
import unittest
from animais import Animal
from recintos import Recinto

class TestRecinto(unittest.TestCase):
    def test_adicionar_animal(self):
        recinto = Recinto("Savana", "Felino")
        animal = Animal("Leão", "Felino", 50)
        recinto.adicionar_animal(animal)
        self.assertIn(animal, recinto.animais)

if __name__ == '__main__':
    unittest.main()
```

Este teste verifica se o método `adicionar_animal` da classe `Recinto` funciona corretamente ao adicionar um animal à lista de animais no recinto.

## Conclusão

Este relatório descreve a estrutura da API de zoológico, incluindo as classes `Animal` e `Recinto`, bem como os testes unitários para garantir seu funcionamento correto.