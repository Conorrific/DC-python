class Store:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        print("My Store")

    def open(self):
        print("Open")

shoe_store = Store('My Shoe Store','1200 Richmond Ave')
shoe_store.open()

print(shoe_store.name)