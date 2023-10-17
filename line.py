from beverage import Beverage

class Line:
    def __init__(self, number) -> None:
        self._number = number
        self.beverage:Beverage = None
        self._number_beverage:int = None

    def add_beverage(self, beverage: Beverage, number_beverage):
        self._name = beverage.name
        self.beverage = beverage
        self._number_beverage = number_beverage
        return "added"
    
    def getinfo(self):
        return f' in {self._number} -- line , {self.beverage}, number of drinks {self._number_beverage}'

    def get_price(self, name):
        beverage = self.beverage
        if beverage == None:
            return None
        elif name == beverage.name:
            return self.beverage.price
        return None



    