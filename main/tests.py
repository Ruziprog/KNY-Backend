from django.test import TestCase
from .models import Character, Demon


class CharacterModelTest(TestCase):
    def setUp(self):
        self.character = Character.objects.create(name="Кибуцуджи Музан", title="Главный Злодей", description="Первый демон, убийца семьи Камадо", ability="Криокинезис", order=1)
        self.demon = Demon.objects.create(name="Аказа", rank="Верховный демон", description="Ищет сильнейших противников", blood_art="Смертельный Компас")

    def test_character_creation(self):
        self.assertEqual(self.character.title, "Главный Злодей")
        self.assertEqual(self.character.description, "Первый демон, убийца семьи Камадо")
        self.assertEqual(self.character.ability, "Криокинезис")

    def test_demon_creation(self):
        self.assertEqual(self.demon.rank, "Верховный демон")
        self.assertEqual(self.demon.description, "Ищет сильнейших противников")
        self.assertEqual(self.demon.blood_art, "Смертельный Компас")

    def test_character_str_method(self):
        self.assertEqual(str(self.character), "Кибуцуджи Музан")

    def test_demon_str_method(self):
        self.assertEqual(str(self.demon), "Аказа")

    def test_character_ordering(self):
        char1 = Character.objects.create(name="Камадо Танджиро", order=2)
        char2 = Character.objects.create(name="Незуко Камадо", order=3)
        characters = Character.objects.all()
        self.assertEqual(list(characters), [self.character, char1, char2])

    def test_hashira_filter(self):
        hashira = Character.objects.create(name="Томиока Гию", is_hashira=True)
        non_hashira = Character.objects.create(name="Зеницу Агацума", is_hashira=False)
        hashira_list = Character.objects.filter(is_hashira=True)
        self.assertIn(hashira, hashira_list)
        self.assertNotIn(non_hashira, hashira_list)

    def test_demon_rank_filter(self):
        demon1 = Demon.objects.create(name="Аказа", rank="Верховный демон", description="Ищет сильнейших противников", blood_art="Смертельный Компас")
        demon2 = Demon.objects.create(name="Руи", rank="Нижний демон", description="Пытается собрать свою паучью семью", blood_art="Паутина из крови")
        demons = Demon.objects.filter(rank="Верховный демон")
        self.assertIn(demon1, demons)
        self.assertNotIn(demon2, demons)
    
    def test_demon_rank_nullable(self):
        demon = Demon.objects.create(name="Безранговый демон", description="Демон без ранга", blood_art="Теневой Клинок")
        self.assertIsNone(demon.rank)

    def test_character_title_nullable(self):
        character = Character.objects.create(name="Безтитульный персонаж", description="Персонаж без титула", ability="Невидимость")
        self.assertIsNone(character.title)