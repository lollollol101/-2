class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name=name
        self._quantity=quantity
        self.unit=unit
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        value=float(value)
        if value<=0:
            raise ValueError('Количество должно быть положительным')
        self._quantity=value

    def __str__(self):
        return f'{self.name}: {self.quantity} {self.unit}'
    
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        return self.name==other.name and self.unit==other.unit

 
class Recipe:
    def __init__(self, title: str, ingredients):
        self.title=title
        self.ingredients=ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for i in self.ingredients:
            if i==ingredient:
                i.quantity+=ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int, float)):
            if ratio>0:
                return True
        return False

    def scale(self, ratio: float):
        if self.is_valid_ratio(ratio): #в задании чётко не прописана надбность проверки, но наврное метод для этого
            ingredients_1=[]
            for i in self.ingredients:
                ingredient_1=Ingredient(i.name, i.quantity*ratio, i.unit)
                ingredients_1.append(ingredient_1)
            return Recipe(self.title, ingredients_1)
        else:
            raise ValueError("Ratio должно быль положительным")

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        s= f'{self.title}\n'
        s+=f'Список ингридиентов\n'
        for i in self.ingredients:
            s+=f'{i}\n'
        return s
    
    