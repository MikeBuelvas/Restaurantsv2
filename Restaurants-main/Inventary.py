import pickle
from typing import Optional
import Drink

class Inventary():
    def __init__(self) -> None:
        
        #self.ingredients
        archive_ingredients = open("archive_ingredients","ab+")
        archive_ingredients.seek(0)
        try:
            self.ingredients = pickle.load(archive_ingredients)        
        except:
            self.ingredients = []
        finally:
            archive_ingredients.close()
            del(archive_ingredients)
        
        #self.drinks
        archive_drinks = open("archive_drinks","ab+")
        archive_drinks.seek(0)
        try:
            self.drinks = pickle.load(archive_drinks)        
        except:
            self.drinks = []
        finally:
            archive_drinks.close()
            del(archive_drinks)
        
    
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
        self.save_d()

    def remove_drink(self, drink):
        for x in range(len(self.drinks)):
            if self.drinks[x] == drink:
                if self.drinks[x].cuantity > 0:
                    self.drinks[x].cuantity-=1
        
        self.save_d()         


    def save_d(self) -> None:
            archive_drinks = open("archive_drinks","wb")
            pickle.dump(self.drinks, archive_drinks)
            archive_drinks.close()
            del(archive_drinks)

    def save_i(self) -> None:
            archive_ingredients = open("archive_ingredients","wb")
            pickle.dump(self.drinks, archive_ingredients)
            archive_ingredients.close()
            del(archive_ingredients)
