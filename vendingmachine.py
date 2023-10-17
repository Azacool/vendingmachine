from beverage import Beverage
from line import Line
from card import Card

class VendingMachine:
    def __init__(self) -> None:
        self.card_list: list[Card] = []
        self.line_list = [Line(i) for i in range(1, 7)]

    def add_beverage(self, line, beverage: Beverage, number_beverage):
        line = self.line_list[line-1]
        return line.add_beverage(beverage, number_beverage)

    def info(self, line):
        line = self.line_list[line-1]
        return line.getinfo()

    def get_price(self, name):
        for line in self.line_list:
            check = line.get_price(name)
            if  check != None:
                return check
        return -1.0

    def recharge_card(self, id, debit):
        for card in self.card_list:
            if card._id == id:
                card.add_sum(debit)
                print(f"to {id} this amount of soum {debit} is added,and total amount in the card is {card.cretid}")
                return
        card = Card(id, debit)
        self.card_list.append(card)
        print("card is added")
 
    
    def getCredit(self, card_id):
        for card in self.card_list:
            if card._id == card_id:
                return card.cretid
        return -1.0

  
    def refill_column(self, column_number, drink_name, number_of_cans):
        if column_number < 1 or column_number > len(self.line_list):
            print(f"Invalid column number: {column_number}")
            return
        
        line = self.line_list[column_number - 1]
        beverage = Beverage(drink_name, 0)  
        result = line.add_beverage(beverage, number_of_cans)

        if result == "added":
            print(f"Refilled column {column_number} with {drink_name} ({number_of_cans} cans)")
        else:
            print(f"Failed to refill column {column_number} with {drink_name} ({result})")

    def available_cans(self) : 
        total_available_cans = 0
        for line in self.line_list:
            if line.beverage is not None:
                total_available_cans += line._number_beverage
        return total_available_cans


 
