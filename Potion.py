class Potion:
    def __init__(self, potion_type, name, amount, price, sort_key):
        self.type = potion_type
        self.name = name
        self.amount = amount
        self.price = price
        self._sort_key = sort_key

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

    def __str__(self):
        return (f"Potion Type: {self.type}"
                f"Potion Name: {self.name}"
                f"\nPotion Effect: {self.amount}"
                f"\nPrice: {self.price}")

    def __gt__(self, other):
        return self.sort_key >= other.sort_key
    def __lt__(self, other):
        return self.sort_key <= other.sort_key
    def __eq__(self, other):
        return self.sort_key == other.sort_key