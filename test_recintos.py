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
