import pickle
import Saucer, Inventary


class Kitchen():
    def __init__(
            self          
    ) -> None:
        self.inventary = Inventary()
        self.orders = []
        archive_saucers = open("archive_saucers","ab+")
        archive_saucers.seek(0)
        try:
            self.saucers = pickle.load(archive_saucers)        
        except:
            self.saucers = []
        finally:
            archive_saucers.close()
            del(archive_saucers)

    def create_saucer(
            self,
            name: str,
            ingredients: list,
            description: str,
            price: float        
    ) -> None:
        saucer = Saucer(name,ingredients,description,price)
        self.Saucers.append(saucer)
        self.save_s()

    def cook_saucer(self, saucer: Saucer) -> None:
        for ingredient in saucer.ingredients:
            for x in range(len(self.inventary.ingredients)):
                if self.inventary.ingredients[x] == ingredient:
                    if self.inventary.ingredients[x][1] > 0:
                        self.inventary.ingredients[x][1]-=1
        
        self.inventary.save_i()
                    
    
    def save_s(self) -> None:
            archive_saucers = open("archive_saucers","wb")
            pickle.dump(self.saucers, archive_saucers)
            archive_saucers.close()
            del(archive_saucers)
