class CoffeeMachine:
    # Features : Welcome Screen
    # actions: buy, fill, take, remaining, exit
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def welcome_machine(self):
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
{self.money} of money""")

    def esp_resource_check(self):
        if self.water >= 250 and self.coffee_beans >= 16 and self.disposable_cups >= 1:
            return True
        return False

    def latte_resource_check(self):
        if self.water >= 350 and self.milk > 75 and self.coffee_beans >= 20 and self.disposable_cups >= 1:
            return True
        return False

    def capp_resource_check(self):
        if self.water >= 200 and self.milk > 100 and self.coffee_beans >= 12 and self.disposable_cups >= 1:
            return True
        return False

    def buy(self, item):
        if item == 'espresso':
            if self.esp_resource_check():
                print(f"I have enough resources, making you a {item}!")
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.disposable_cups -= 1
            else:
                if self.water < 250:
                    print("Sorry, not enough water!")
                elif self.coffee_beans < 16:
                    print("Sorry, not enough coffee_beans!")


        elif item == 'cappuccino':
            if self.capp_resource_check():
                print(f"I have enough resources, making you a {item}!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.disposable_cups -= 1
                self.money += 6
            else:
                if self.water < 200:
                    print("Sorry, not enough water!")
                elif self.coffee_beans < 12:
                    print("Sorry, not enough coffee_beans!")
                elif self.milk < 100:
                    print("Sorry, not enough milk!")

        elif item == 'latte':
            if self.latte_resource_check():
                print(f"I have enough resources, making you a {item}!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.disposable_cups -= 1
            else:
                if self.water < 350:
                    print("Sorry, not enough water!")
                elif self.coffee_beans < 20:
                    print("Sorry, not enough coffee_beans!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def remaining(self):
        self.welcome_machine()

    def exit(self):
        exit()


my_machine = CoffeeMachine()


def choose_menu(item):
    if item == '1':
        return 'espresso'
    elif item == '2':
        return 'latte'
    elif item == '3':
        return 'cappuccino'
    elif item == 'back':
        pass


while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == 'remaining':
        my_machine.welcome_machine()
    elif action == 'buy':
        item = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        my_machine.buy(choose_menu(item))
    elif action == 'fill':
        my_machine.fill()
    elif action == 'take':
        my_machine.take()
    elif action == 'exit':
        my_machine.exit()
