import unittest
import PartA

phone = PartA.Phone("iPhone", "16 Pro Max", 2024, 999, "Gray")
laptop = PartA.Laptop("Macbook", "Air M1", 2020, 1024, "Blue", "Magic Keyboard", "Magic Trackpad")

class TestPartA(unittest.TestCase):
    def test_is_instance_of_phone(self):
        self.assertIsInstance(phone, PartA.Phone)

    def test_is_instance_of_laptop(self):
        self.assertIsInstance(laptop, PartA.Laptop)

    #I tried this but it seems that if you are a subclass that also counts as an instance of the main class
    #def test_is_not_instance_of_phone(self):
        #self.assertNotIsInstance(laptop, PartA.Phone)

    #Instead I will do this test
    def test_is_instance_of_a_subclass_of_phone(self):
        self.assertIsInstance(laptop, PartA.Phone)

    def test_is_not_instance_of_laptop(self):
        self.assertNotIsInstance(phone, PartA.Laptop)

    def test_objects_are_identical(self):
        phone2 = phone
        self.assertIs(phone, phone2)

    def test_objects_are_not_identical(self):
        phone2 = PartA.Phone("Samsung", "Galaxy S25", 2025, 1000, "Pink")
        self.assertIsNot(phone, phone2)

    def test_update_methods(self):
        phone.set_brand("Samsung")
        self.assertEqual(phone.brand, "Samsung")
        
        phone.set_model("Galaxy S25")
        self.assertEqual(phone.model, "Galaxy S25")
        
        phone.set_year(2021)
        self.assertEqual(phone.year, 2021)
        
        phone.set_price(500)
        self.assertEqual(phone.price, 500)
        
        phone.set_colour("Pink")
        self.assertEqual(phone.colour, "Pink")

        laptop.set_brand("Microsoft")
        self.assertEqual(laptop.brand, "Microsoft")

        laptop.set_model("Surface")
        self.assertEqual(laptop.model, "Surface")

        laptop.set_year(2023)
        self.assertEqual(laptop.year, 2023)

        laptop.set_price(800)
        self.assertEqual(laptop.price, 800)


        laptop.set_colour("White")
        self.assertEqual(laptop.colour, "White")


        laptop.set_keyboard("Chiclet")
        self.assertEqual(laptop.keyboard, "Chiclet")

        laptop.set_trackpad("M-Pad")
        self.assertEqual(laptop.trackpad, "M-Pad")

def main():
    unittest.main()

if __name__ == '__main__':
    main()