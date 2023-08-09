class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contact_Details(self):
        print("To contact us, log on to ", self.contactWebsite)

class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacturer = 2017

    def manufacturerDetails(self):
        # print("This Macbook was manufacturer in the year {} by {}".format(self.yearOfManufacturer, self.manufacturer))
        print(f"This Macbook was manufacturer in the year {self.yearOfManufacturer} by {self.manufacturer}")

macbook = Macbook()
macbook.manufacturerDetails()
macbook.contact_Details()