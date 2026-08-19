class Potion:
    potions = {}
    def __init__(self, description, potion_type, name, amount, price, sort_key):
        self._description = description
        self.type = potion_type
        self.name = name
        self.amount = amount
        self.price = price
        self._sort_key = sort_key
        Potion.potions[name] = self

    @property
    def description(self):
        return self._description

    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, new_t):
        self._type = new_t

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_n):
        self._name = new_n

    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, new_amount):
        self._amount = new_amount

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, amount):
        self._price = amount

    @property
    def sort_key(self):
        return self._sort_key

    def show_info(self):
        print(f"Potion type: {self.type} | Name: {self.name} \n"
              f"Info: {self.description}\n"
              f"Potion effect: {self.amount} | Price: {self.price} \n")

    def __str__(self):
        return f"{self.type}{self.name}{self.amount}{self.price}"

    def __gt__(self, other):
        return self.sort_key > other.sort_key
    def __lt__(self, other):
        return self.sort_key < other.sort_key
    def __eq__(self, other):
        return self.sort_key == other.sort_key