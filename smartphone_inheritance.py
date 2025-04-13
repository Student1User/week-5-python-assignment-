# Smartphone class with encapsulation and inheritance
class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.__battery_level = battery_level  # Private attribute for battery level

    # Public method to charge the phone
    def charge(self, amount):
        self.__battery_level = min(100, self.__battery_level + amount)
        print(f"{self.brand} {self.model} is charging. Battery level is now {self.__battery_level}%.")

    # Public method to make a call
    def make_call(self, number):
        if self.__battery_level > 10:
            print(f"Calling {number}... 📞")
            self.__battery_level -= 5
        else:
            print("Battery too low to make a call. Please charge your phone.")
    
    # Public method to check battery status
    def battery_status(self):
        print(f"Battery level: {self.__battery_level}%.")

# Inheriting from Smartphone to create a feature-rich class
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_level, camera_quality):
        super().__init__(brand, model, battery_level)  # Inherit from Smartphone
        self.camera_quality = camera_quality

    # Method to take a picture
    def take_picture(self):
        print(f"Taking a picture with {self.camera_quality} camera quality... 📸")

# Creating an object of SmartphoneWithCamera class
phone = SmartphoneWithCamera("Apple", "iPhone 14", 85, "108MP")
phone.charge(10)
phone.make_call("+1234567890")
phone.take_picture()
phone.battery_status()
