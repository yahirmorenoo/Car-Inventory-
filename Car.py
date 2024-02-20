#car.py
class Car(): 
    def __init__(self, make, model, year, price): 
        self.make = make.upper()
        self.model = model.upper()
        self.year = year 
        self.price = price

    def __gt__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    return self.price > rhs.price
                else:
                    return self.year > rhs.year
            else:
                return self.model > rhs.model

        else:
            return self.make > rhs.make


    def __eq__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return True
        else:
            return False

        
    
    def __lt__(self, rhs): 

        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    return self.price < rhs.price
                else:
                    return self.year < rhs.year
            else:
                return self.model < rhs.model

        else:
            return self.make < rhs.make
         

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}".format(self.make, self.model, self.year, self.price)



