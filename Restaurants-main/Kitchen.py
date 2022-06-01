from typing import Optional
import Saucer, Inventary


class Kitchen():
    def __init__(
            self,
            inventary: Inventary,
            saucers: Optional[list] = None
            
    ) -> None:
        self.inventary = inventary
        self.saucers = saucers

    def create_saucer(
            self,
            name: str,
            ingredients: list,
            description: str,
            price: float        
    ) -> None:
        saucer = Saucer(name,ingredients,description,price)
        self.Saucers.append(saucer)

    def cook_saucer(self, saucer: Saucer) -> None:
        for ingredient in saucer.ingredients:
            for x in range(len(self.inventary.ingredients)):
                if self.inventary.ingredients[x] == ingredient:
                    if self.inventary.ingredients[x][1] > 0:
                        self.inventary.ingredients[x][1]-=1
                    else:
                        pass
                
    