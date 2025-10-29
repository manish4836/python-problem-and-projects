class Mobile:
    def __init__(self, brand, model, batterry = 100):
        self.brand = brand
        self.model = model
        self.battery = batterry
        self.is_on = False

        print(f" New {self.brand} {self.model} created!")
        print(f" Initial Battery: {self.battery}%")

    def turn_on(self):
        if not self.is_on :
            self.is_on = True
            print(f"{self.brand} {self.model} turned ON!")
        else:
            print(f"{self.brand} is already ON!")

    def turn_off(self):
        if not self.is_on :
            self.is_on = False
            print(f"{self.brand} {self.model} turned OFF!")
        else:
            print(f"{self.brand} is already OFF!")

            

    def use_phone(self, minutes):
        if self.is_on:
            if self.battery > 0:
                # Each minute uses 2% battery
                battery_used = minutes * 2
                self.battery -= battery_used
                
                # Battery can't go below 0
                if self.battery < 0:
                    self.battery = 0
                    print(f"📱 {self.brand} battery died! Please charge.")
                else:
                    print(f"📱 Used {self.brand} for {minutes} minutes. Battery used: {battery_used}%")
                    print(f"🔋 Remaining Battery: {self.battery}%")
            else:
                print(f"❌ {self.brand} battery is dead. Please charge first.")
        else:
            print(f"❌ Please turn ON the phone first!")

    def charge_phone(self, minutes=10):
        # Each minute charges 5% battery
        charge_amount = minutes * 5
        self.battery += charge_amount
        
        # Battery can't go above 100
        if self.battery > 100:
            self.battery = 100
            print(f"🔋 {self.brand} fully charged! (100%)")
        else:
            print(f"🔋 {self.brand} charged for {minutes} minutes. Battery: {self.battery}%")

    def display_info(self):
        status = "ON" if self.is_on else "OFF"
        print(f"\n📱 Mobile Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery: {self.battery}%")
        print(f"Status: {status}")


# Mobile phones banayein
phone1 = Mobile("Samsung", "Galaxy S21", 80)
phone2 = Mobile("iPhone", "14 Pro")

print("=" * 40)

# Phone 1 operations
phone1.display_info()
phone1.turn_on()
phone1.use_phone(10)  # Use for 10 minutes
phone1.use_phone(20)  # Use for 20 minutes
phone1.charge_phone(5)  # Charge for 5 minutes
phone1.display_info()

print("=" * 40)

# Phone 2 operations  
phone2.turn_on()
phone2.use_phone(30)  # Use for 30 minutes
phone2.use_phone(40)  # Use more - battery might die
phone2.charge_phone(15)  # Full charge
phone2.turn_off()
phone2.display_info()