class Phone:
    def __init__(self, brand, model, year, price, colour):
        self.brand = str(brand)
        self.model = str(model)
        self.year = int(year)
        self.price = float(price)
        self.colour = str(colour)
    
    def print(self):
        print(self.brand, self.model, self.year, self.price, self.colour)

    def set_brand(self, new_brand):
        self.brand = str(new_brand)

    def set_model(self, new_model):
        self.model = str(new_model)
    
    def set_year(self, new_year):
        if new_year >= 0:
            self.year = int(new_year)
        else:
            print("Year cant be negative")
    
    def set_price(self, new_price):
        if new_price >= 0 :
            self.price = float(new_price)
        else:
            print("Price cant be negative")
    
    def set_colour(self, new_colour):
        self.colour = str(new_colour)

class Laptop(Phone):
    def __init__(self, brand, model, year, price, colour, keyboard, trackpad):
        super().__init__(brand, model, year, price, colour) 
        self.keyboard = str(keyboard)
        self.trackpad = str(trackpad)
    
    #overrided it to keep it on same line
    def print(self):
        print(self.brand, self.model, self.year, self.price, self.colour, self.keyboard, self.trackpad)

    def set_keyboard(self, new_keyboard):
        self.keyboard = str(new_keyboard)
    
    def set_trackpad(self, new_trackpad):
        self.trackpad = str(new_trackpad)

    
    

phone = Phone("iPhone", "16 Pro Max", 2024, 999, "Gray")
phone.print()

phone.set_brand("Samsung")
phone.set_model("Galaxy S25")
phone.set_year(2025)
phone.set_price(1000)
phone.set_colour("Pink")

phone.print()

laptop = Laptop("Macbook", "Air M1", 2020, 1024, "Blue", "Magic Keyboard","Magic Trackpad")
laptop.print()

laptop.set_brand("Microsoft")
laptop.set_model("Surface")
laptop.set_year(2023)
laptop.set_price(800)
laptop.set_colour("White")
laptop.set_keyboard("Chiclet")
laptop.set_trackpad("M-Pad")

laptop.print()

phone.set_price(-1)
phone.set_year(-2025)