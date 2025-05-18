class Toy:
    def __init__(self, new_name, new_colour, new_cost):
        self.name = new_name
        self.colour = new_colour
        self.cost = new_cost


    def __str__(self):
        return f"name: {self.name}\ncolour: {self.colour}\ncost: {self.cost}"
    
class ToyBox:
    def __init__(self, name):
        self.name = name
        self.all_toys = []

    def add_toy(self, name, colour, cost):
        toy = Toy(name, colour, cost)
        self.all_toys.append(toy)

    def total_toys(self):
        return len(self.all_toys)
    
    def total_cost(self):
        cost = 0
        for toy in self.all_toys:
            cost += toy.cost
        return cost
    
    def cheapest_toy(self):
        if not self.all_toys:
            return 'empty box'
        cheapest = self.all_toys[0].cost

        for t in self.all_toys:
            if t.cost < cheapest:
                cheapest = t.cost
        return cheapest

    def __str__(self):
        cheap = self.cheapest_toy()
        totalcost = self.total_cost()
        total = self.total_toys()
        msg = f"{total} {'toys' if total != 1 else 'toy'} in the list"
        for toy in self.all_toys:
            msg += f"\n{toy}\n"
        return msg + f"\nthe total cost is ${totalcost}\nthe cheapest toy is cost for {cheap}"
    
toy = ToyBox('collection')
print(toy.cheapest_toy())
toy.add_toy('bob', 'red', 10)
toy.add_toy('rigor', 'blue', 23)
toy.add_toy('aldous', 'black', 45)
print(toy)
cheapest = toy.cheapest_toy()
print(f'{cheapest=}')


        


        