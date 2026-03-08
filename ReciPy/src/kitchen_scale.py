class Kitchen_Scale:
    def __init__(self, name):
        """
        Initialize a Kitchen_Scale instance

        Attributes:
            name (str): the name or identifier of the scale
        """
        self.name = name

class Weight_Scale(Kitchen_Scale):
    def __init__(self, name = None, grams_per_unit = None):
        """
        Initialize a Weight_Scale instance

        Attributes:
            name (str): The name or identifier of the scale
            grams_per_unit (dict): Mapping of units to their gram equivalent
        """
        grams_per_unit = {'g': 1, 'kg': 1000, 'oz': 28.349523125, 'lb': 453.59237}        
        super().__init__(name)
        self.grams_per_unit = grams_per_unit

    def convert_weight(self, amount: float, from_unit: str, to_unit: str) -> float:
        """
        Convert `amount` from `from_unit` to `to_unit`.

        Args:
            amount (float): The numeric amount to convert.
            from_unit (str): The unit of the input amount.
            to_unit (str): The desired output unit.

        Returns:
            float: The converted amount rounded to 3 decimal places.
        """
        fu = str(from_unit).lower()
        tu = str(to_unit).lower()

        if fu not in self.grams_per_unit:
            raise ValueError(f"Unsupported from_unit: '{from_unit}'. Units must be specified like 'g' for grams")

        if tu not in self.grams_per_unit:
            raise ValueError(f"Unsupported to_unit: '{to_unit}'. Units must be specified like 'g' for grams")

        # Converting input to grams
        grams = float(amount) * self.grams_per_unit[fu]

        # Converting grams to `to_unit`
        result = grams / self.grams_per_unit[tu]
        
		# Rounding to 3 decimal places
        result = round(result, 3)

        return result

class Volume_Scale(Kitchen_Scale):
    def __init__(self, name = None, milliliters_per_unit = None):
        """
        Initialize a Volume_Scale instance

        Attributes:
            name (str): The name or identifier of the scale
            milliliters_per_unit (dict): Mapping of units to their milliliter equivalent
        """
        milliliters_per_unit = {'ml': 1, 'l': 1000, 'tsp': 4.92892, 'c': 237, 'gal': 3785.41}
        super().__init__(name)
        self.milliliters_per_unit = milliliters_per_unit

    def convert_volume(self, amount: float, from_unit: str, to_unit: str) -> float:
        """
        Convert `amount` from `from_unit` to `to_unit`.

        Args:
            amount (float): The numeric amount to convert.
            from_unit (str): The unit of the input amount.
            to_unit (str): The desired output unit.

        Returns:
            float: The converted amount rounded to 3 decimal places.
        """
        fu = str(from_unit).lower()
        tu = str(to_unit).lower()

        if fu not in self.milliliters_per_unit:
            raise ValueError(f"Unsupported from_unit: '{from_unit}'. Units must be specified like 'ml' for milliliters")

        if tu not in self.milliliters_per_unit:
            raise ValueError(f"Unsupported to_unit: '{to_unit}'. Units must be specified like 'ml' for milliliters")

        # Converting input to milliliters
        grams = float(amount) * self.milliliters_per_unit[fu]

        # Converting milliliters to `to_unit`
        result = grams / self.milliliters_per_unit[tu]
        
		# Rounding to 3 decimal places
        result = round(result, 3)

        return result
