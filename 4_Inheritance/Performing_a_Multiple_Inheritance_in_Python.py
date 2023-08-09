class OperatingSystem:
    multitasking = True
    name = "Mac OS"

class Apple:
    website = "www.apple.com"
    name = "Apple"

class Macbook(Apple, OperatingSystem):
    def __init__(self):
        if self.multitasking:
            print(f"This is multi tasking system. Visit {self.website} for more details")
            print(f"Name: {self.name}")
macBook = Macbook()