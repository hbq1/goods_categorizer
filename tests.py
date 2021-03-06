import unittest

from .categorizer import Categorizer


class CategorizerTestCases(unittest.TestCase):

    def setUp(self):
        self.categorizer = Categorizer('dict_of_mined_goods.json')
        self.names = [
            u'молоко "Домик в Деревне" 2л',
            u'Подушка "ваше счастье" икеа',
            u'хлеб черный Дарницкий 1234гр',
            u'Томаты сливовидные 1 кг',
            u'Сливки Романов луг стерилизованные 10% 200 г',
            u'Картофель мытый упакованный 1 кг',
            u'Огурец длинноплодный 1 шт'
        ]

    def test_exist_result(self):
        for t in self.names:
            self.assertIsNotNone(self.categorizer.get_сategory(t))


if __name__ == '__main__':
    unittest.main()