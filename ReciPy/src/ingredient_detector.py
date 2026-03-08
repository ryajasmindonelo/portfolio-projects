import random

class IngredientDetector:
    """
    Stores lists of ingredients that are not allowed for dairy-free and vegan diets.
    Provides methods to check if ingredients violate dietary restrictions.
    """

    def __init__(self):
        """ 
        Initializes IngredientDetector and creates lists of banned ingredients
        for dairy-free and vegan diets.

        Attributes:
            dairy_free_banned (list): A list of ingredients incompatible with a dairy allergy
            vegan_banned (list): A list of ingredients incompatible with a vegan diet
        """

        # list of ingredients not allowed for dairy-free diet
        self.dairy_free_banned = [
            "butter", "buttermilk", "butter fat",
            "casein", "cheese", "cottage cheese",
            "cream cheese", "cream", "curds", "ghee",
            "lactaid milk", "lactoglobulin", "lactose",
            "sour cream", "yogurt", "whey", "rennet",
            "recaldent", "lactalbumin", "lactalbumin phosphate",
            "milk", "milk derivative", "milk protein",
            "milk solids", "malted milk", "condensed milk",
            "evaporated milk", "dry milk", "whole milk",
            "low-fat milk", "non-fat milk", "skim milk",
            "milk fat", "milk salt",
            "ammonium caseinate", "calcium caseinate",
            "magnesium caseinate", "potassium caseinate",
            "sodium caseinate", "caseinates",
            "casein hydrolysate", "milk protein hydrolysate",
            "protein hydrolysate", "whey hydrolysate"
        ]

        # vegan list includes dairy-free banned  and extra non-vegan items
        self.vegan_banned = self.dairy_free_banned + [
            "egg", "eggs", "honey", "gelatin",
            "meat", "fish", "shellfish", "poultry", "chicken",
            "beef", "pork", "shrimp", "clam", "clams", "oyster", "oysters",
        ]


    def isAllergen(self, ingredient: str, diet_type: str) -> bool:
        """ 
        Returns True or False depending on whether the ingredient violates
        a dietary restriction.

        Args:
        ingredient (str): the ingredient to check
        diet_type (str): either "dairy-free" or "vegan"
        
        Returns:
            bool: True if ingredient is not allowed, False otherwise
        """

        ingredient = ingredient.lower()   ## convert input to lowercase

        # check if ingredient is banned for dairy-free
        if diet_type == "dairy-free":
            return ingredient in self.dairy_free_banned

        # check if ingredient is banned for vegan diet
        if diet_type == "vegan":
            return ingredient in self.vegan_banned

        return False   # default return if diet_type is invalid


    def detectIngredients(self, ingredient_list: list) -> dict:
        """ 
        Returns a dictionary showing whether each ingredient in the list
        is dairy-free and vegan friendly.

        Args:
            ingredient_list (list): ingredients to evaluate
        
        Returns:
            dict: dictionary with ✅ (allowed) and ❌ (not allowed)
        """

        # dictionary to store final results for both diets
        result = {
            "dairy-free": {},
            "vegan": {}
        }

        # loop through each ingredient provided by the user
        for item in ingredient_list:
            item_lower = item.lower()   # convert item to lowercase

            # dairy-free evaluation
            if item_lower in self.dairy_free_banned:
                result["dairy-free"][item] = "❌"   # not allowed
            else:
                result["dairy-free"][item] = "✅"   # allowed

            # vegan evaluation
            if item_lower in self.vegan_banned:
                result["vegan"][item] = "❌"   # not allowed
            else:
                result["vegan"][item] = "✅"   # allowed

        return result   # return full evaluation dictionary
    

    def generateRecipe(self, ingredients: list) -> dict:
        """
        Generate one simple mad-libs style recipe for a given list of ingredients

       Args:
            ingredients (list): A list of ingredients, all formatted as strings

        Returns:
            dict: A dictionary containing the final recipe title, ingredients used, and recipe instructions
        """
        # ensures all ingredients are strings, and that at least one ingredient is passed through
        cleaned = []
        for ingredient in ingredients:
            if not isinstance(ingredient, str):
                raise TypeError("all ingredients must be strings.")
            stripped = ingredient.strip()
            if stripped:
                cleaned.append(stripped)
        if not cleaned:
            raise ValueError("ingredients must contain at least one non-empty string.")

        # Recipe templates
        templates = [
            ("Roasted {0} with {1}", 2, [
                "Preheat the oven to 400°F. Pat the {0} dry and season.",
                "Roast the {0} until tender, then toss with {1}.",
                "Serve warm with extra {1} on top."
            ]),
            ("{0} & {1} Toss", 2, [
                "Chop the {0} and {1} into bite-sized pieces.",
                "Toss {0} and {1} with oil, salt, and pepper.",
                "Serve chilled or at room temperature."
            ]),
            ("Quick {0} and {1} Sauté", 2, [
                "Heat a skillet and add a splash of oil.",
                "Sauté {0} until slightly browned, then add {1}.",
                "Cook another 2–3 minutes and finish with a squeeze of lemon."
            ]),
            ("{0}, {1} and {2} Delight", 3, [
                "Combine {0}, {1} and {2} in a large bowl.",
                "Toss with dressing and let flavors meld for 10 minutes.",
                "Serve with crusty bread or over rice."
            ]),
            ("{} Smoothie", 1, [
                "Place the {0} in a blender.",
                "Blend until smooth and creamy.",
                "Pour into a glass and enjoy immediately."
            ])
        ]

        # Filter for compatible templates
        available = len(cleaned)
        compatible_recipe = [recipe for recipe in templates if recipe[1] <= available]
        if not compatible_recipe:
            raise ValueError(f"No recipe templates can be filled with {available} ingredient(s).")

        # Assign random template and ingredient order
        title_template, slots, steps = random.choice(compatible_recipe)
        chosen_ingredients = random.sample(cleaned, k=slots)

        # Formatting the recipe
        title = title_template.format(*chosen_ingredients)
        filled_steps = [step.format(*chosen_ingredients) for step in steps]
        instructions = "\n".join(filled_steps)

        return {
            "title": title,
            "ingredients_used": chosen_ingredients,
            "instructions": instructions
        }