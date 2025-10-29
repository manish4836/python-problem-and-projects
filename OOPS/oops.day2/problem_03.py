class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0
        self.engine_on = False
        print(f" New {self.color}, {self.brand}, {self.model} created!")

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print(f"{self.brand}, {self.model} engine started!")
        else:
             print(f"{self.brand} engine is already running!")
    def accelerate(self):
        if self.engine_on :
            self.speed += 10
            print(f" {self.brand} accelerating... Current speed: {self.speed} km/h")
        else:
            print(f" Please start the engine first!")

    def brake(self):
        if self.speed > 0:
            self.speed -= 5  
            print(f" {self.brand} braking... Current speed: {self.speed} km/h")
        else:
            print(f" {self.brand} is already stopped!")

    def display_info(self):
        engine_status = "ON" if self.engine_on else "OFF"
        print(f"\n Car Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed} km/h")
        print(f"Engine: {engine_status}")

car1 = Car("Toyota", "Camry", "Red")
car2 = Car("Honda", "Civic", "Blue")

car1.display_info()  

car1.start_engine()
car1.accelerate()    
car1.accelerate()    
car1.brake()         
car1.display_info()  

print("\n" + "="*30)

car2.start_engine()
car2.accelerate()
car2.accelerate()
car2.display_info()