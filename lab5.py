class Toy:
    """
    Represents a toy with a name, colour, and price.

    Attributes:
        name (str): The name of the toy.
        colour (str): The colour of the toy, stored in lowercase.
        price (float): The price of the toy in dollars.
    """
    def __init__(self, new_name, new_colour, new_price, new_toy_type):
        self.name = new_name
        self.colour = new_colour
        self.price = new_price
        self.toy_type = new_toy_type
    def __str__(self):
        return f'A {self.colour.lower()} {self.toy_type.lower()} called {self.name} which cost ${self.price:.2f}'
        
class ToyBox:
    """
    A container class for storing and managing a collection of Toy objects.

    Attributes:
        all_toys (list): A list that stores all added Toy instances.
    """
    def __init__(self):
        self.all_toys = []
    def add_toy(self, name, colour, price, type):
        toy = Toy(name, colour, price, type)
        self.all_toys.append(toy)
        
    def get_total_toys(self):
        return len(self.all_toys)
        
    def get_total_cost(self):
        toys = 0
        for total_toy in self.all_toys:
            toys += total_toy.price
        return toys
        
    def get_cheapest_toy(self):
        if self.get_total_toys() == 0:
            return 'The toy box is empty.'
        cheapest_price = self.all_toys[0].price
        cheapest_name = self.all_toys[0].name
        
        for cheapest_toy in self.all_toys:
            if cheapest_toy.price < cheapest_price:
                cheapest_price = cheapest_toy.price
                cheapest_name = cheapest_toy.name
        return cheapest_name
    
    def find_toy(self, name):
        for toy in self.all_toys:
            if toy.name.lower() == name.lower():
                return toy

    def remove_toy(self, name):
        for toy in self.all_toys:
            if toy.name.lower() == name.lower():
                self.all_toys.remove(toy)
                return True
        return False
    
    
    def get_by_toy_type(self, type):
        
        list = []

        for toy in self.all_toys:
            if toy.toy_type.lower() == type.lower():
                list.append(toy.name)
        if not list:
            return (False, f'There are no toys of type {type} in the toybox')
        
        return (True, list)
       
                    

                
            
    #modified str
    def __str__(self):
        total = self.get_total_toys()
        result = f"The toy box contains {total} toys"
        if not self.all_toys:
            return f"The toy box is empty."
        for toy in self.all_toys:
            result += f"\n{toy}"
        totalcost = self.get_total_cost()
        return f"{result}\nTotal cost: ${totalcost:.2f}"
    



 	

blue_toybox = ToyBox()
print(blue_toybox)
print('Adding toys ...')
blue_toybox.add_toy('toy1', 'colour1', 101.00, 'toytype1')
blue_toybox.add_toy('toy2', 'colour2', 123, 'toytype1')
blue_toybox.add_toy('toy3', 'colour3', 321, 'toytype1')
blue_toybox.add_toy('toy4', 'colour4', 101.00, 'toytype1')
blue_toybox.add_toy('toy5', 'colour5', 11, 'toytype2')
blue_toybox.add_toy('toy6', 'colour6', 12, 'toytype3')
print(blue_toybox)
print()
print(blue_toybox.remove_toy('toy4'))
print(blue_toybox)