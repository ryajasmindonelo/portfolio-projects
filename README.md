# ReciPy

ReciPy is a Python package that can be used by home cooks and bakers to improve their experience in the kitchen! It can also be used by members of the general public if they want to learn more about cooking.

Primary functionalities include the ability to simulate a kitchen scale, receive allergen information for common dietary restrictions, and create new recipes given a list of ingredients.

## Installation

You can install `recipy` by cloning this Git repository and using pip:

1. Clone this git repository by using https://github.com/nicolehychoi/sds-271-final-project.git (HTTPS) or an SSH key
2. In the cloned project package folder, use `pip install .` to install all folder contents

## Dependencies

`ReciPy` requires the `random` package to be installed. No other dependencies are required.

## Note on units

When using the class `kitchen_scale`, please make sure to properly label the following when using within the methods:
1. 'g' for grams
2. 'kg' for kilograms
3. 'oz' for ounces
4. 'lb' for pounds
5. 'ml' for milliliters
6. 'l' for liters
7. 'tsp' for teaspoons
8. 'c' for cups
9. 'gal' for gallons

## Notes on detecting ingredients

The package uses a list of vegan and dairy free list from Johns Hopkins Medicine. Please beware that while the list is from an official source, it can be incomplete.

List of ingredients not allowed for dairy-free diet: butter, buttermilk, butter fat, casein, cheese, cottage cheese, cream cheese, cream, curds, ghee, lactaid milk, lactoglobulin, lactose, sour cream, yogurt, whey, rennet, recaldent, lactalbumin, lactalbumin phosphate, milk, milk derivative, milk protein, milk solids, malted milk, condensed milk, evaporated milk, dry milk, whole milk, low-fat milk, non-fat milk, skim milk, milk fat, milk salt, ammonium caseinate, calcium caseinate, magnesium caseinate, potassium caseinate, sodium caseinate, caseinates, casein hydrolysate, milk protein hydrolysate, protein hydrolysate, whey hydrolysate.

List of ingredients not allowed for dairy-free diet and extra non-vegan items: egg, eggs, honey, gelatin, meat, fish, shellfish, poultry, chicken, beef, pork, shrimp, clam, clams, oyster, oysters.