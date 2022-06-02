from typing import Optional
import Drink

class Inventary():
    def __init__(
            self,
            ingredients: Optional[list] = None,
            drinks: Optional[list] = None      
    ) -> None:
        self.ingredients = ingredients
        self.drinks = drinks
    
    
    def create_drink(self,
            name: str,
            description: str,
            price: float,
            quantity: int        
    ) -> None:
        drink = Drink(name, description, price, quantity)
        self.drinks.append(drink)
    
    def add_ingredient(self, 
            ingredient: str,
            quantity: int
    ) -> None:
        temp = [ingredient, quantity]
        self.ingredients.append(temp)
            
    def add_drink(self,
            drink: Drink,
            quantity: int
    ) -> None:
        temp = [drink, quantity]
        self.drinks.append(temp)

    def remove_drink(self, drink):
        for x in range(len(self.drinks)):
            if self.drinks[x] == drink:
                if self.drinks[x].cuantity > 0:
                    self.drinks[x].cuantity-=1
                else:
                    pass