import unittest
import random
from src.ingredient_detector import IngredientDetector

class TestIngredientDetector(unittest.TestCase):

    def setUp(self):
        self.det = IngredientDetector()

    def test_initialization(self):
        self.assertTrue(len(self.det.dairy_free_banned) > 0)
        self.assertTrue(len(self.det.vegan_banned) > 0)

    def test_isAllergen_dairy_free_true(self):
        self.assertTrue(self.det.isAllergen("milk", "dairy-free"))

    def test_isAllergen_dairy_free_false(self):
        self.assertFalse(self.det.isAllergen("carrot", "dairy-free"))

    def test_isAllergen_vegan_true(self):
        self.assertTrue(self.det.isAllergen("egg", "vegan"))

    def test_isAllergen_vegan_false(self):
        self.assertFalse(self.det.isAllergen("broccoli", "vegan"))

    def test_isAllergen_case_insensitive(self):
        self.assertTrue(self.det.isAllergen("MILK", "dairy-free"))

    def test_isAllergen_unknown_diet(self):
        self.assertFalse(self.det.isAllergen("milk", "keto"))

    def test_detectIngredients_output_structure(self):
        result = self.det.detectIngredients(["Milk", "Carrot"])
        self.assertIn("dairy-free", result)
        self.assertIn("vegan", result)

    def test_detectIngredients_symbols(self):
        result = self.det.detectIngredients(["Milk", "Carrot"])

        self.assertEqual(result["dairy-free"]["Milk"], "❌")
        self.assertEqual(result["dairy-free"]["Carrot"], "✅")

        self.assertEqual(result["vegan"]["Milk"], "❌")
        self.assertEqual(result["vegan"]["Carrot"], "✅")

    def test_detectIngredients_mixed_case(self):
        result = self.det.detectIngredients(["MILK", "carrot"])
        self.assertEqual(result["vegan"]["MILK"], "❌")
        self.assertEqual(result["vegan"]["carrot"], "✅")

    def test_generate_recipe(self):
        random.seed(0)
        user_ingredients = ["banana", "strawberry", "spinach", "oat milk"]
        
        recipe = self.det.generateRecipe(user_ingredients)
        
        # Generated recipe must be a Python dictionary
        self.assertIsInstance(recipe, dict)
     
        # All ingredients in recipe must be from input list
        for ingredient in recipe["ingredients_used"]:
            self.assertIn(ingredient, user_ingredients, f"Ingredient '{ingredient}' not in input list")

        # Number of ingredients must be less than or equal to number of recipe template slots
        self.assertLessEqual(len(recipe["ingredients_used"]), len(user_ingredients))

if __name__ == "__main__":
    unittest.main()
