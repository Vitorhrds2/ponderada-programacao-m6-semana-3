import unittest
from animais import Animal

class TestAnimal(unittest.TestCase):
    def test_alimentar(self):
        animal = Animal("Leão", "Felino", 50)
        animal.alimentar()
        self.assertEqual(animal.nivel_felicidade, 60)

if __name__ == '__main__':
    unittest.main()
