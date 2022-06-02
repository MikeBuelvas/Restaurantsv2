class Saucer:
    def __init__(
            self,
            name: str,
            ingredients: list,
            description: str,
            price: float        
    ) -> None:
        self.name = name
        self.ingredients = ingredients
        self.description = description
        self.price = price