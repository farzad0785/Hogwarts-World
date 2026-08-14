from random import randint

class Spell:
    spells = {}
    sorter = 1
    def __init__(self, name, description, spell_type, kind, amount, required_level, learning_chance, attempts, token_cost=1):
        self.name = name
        self.description = description
        self.spell_type = spell_type
        self.kind = kind
        self.amount = amount
        self.required_level = required_level
        self.learning_chance = learning_chance
        self.attempts = attempts
        self.token_cost = token_cost
        self.sort_key = Spell.sorter + len(Spell.spells)
        Spell.spells[name] = self

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_n):
        self._name = new_n

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def spell_type(self):
        return self._spell_type
    @spell_type.setter
    def spell_type(self, new_type):
        self._spell_type = new_type

    @property
    def kind(self):
        return self._kind
    @kind.setter
    def kind(self, new_kind):
        self._kind = new_kind

    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, new_amount):
        self._amount = new_amount

    @property
    def required_level(self):
        return self._required_level
    @required_level.setter
    def required_level(self, new_level):
        self._required_level = new_level

    @property
    def learning_chance(self):
        return int(self._learning_chance * 100)
    @learning_chance.setter
    def learning_chance(self, new_chance):
        self._learning_chance = new_chance

    @property
    def token_cost(self):
        return self._token_cost
    @token_cost.setter
    def token_cost(self, new_cost):
        self._token_cost = new_cost

    @property
    def attempts(self):
        return self._attempts
    @attempts.setter
    def attempts(self, amount):
        self._attempts = amount

    def __str__(self):
        return (f"{self.spell_type}{self.name}{self.kind}{self.amount}{self.required_level}{self.learning_chance}"
                f"{self.attempts}{self.token_cost}"
                f"\nInfo: {self.description}")

    def __ge__(self, other):
        return self.sort_key > other.sort_key
    def __lt__(self, other):
        return self.sort_key < other.sort_key

Spell("Bombarda", "Unleashes a paltry burst of ruinous fire.",
      "Spell", "Offensive", randint(5, 15), 1, 1, 0)

Spell("Deprimo", "Crushing weight descends upon the foe, rending flesh and bone to shards.",
      "Spell", "Offensive", randint(1, 10), 1, 1, 0)

Spell("Ebublio", "Traps the hapless soul within a glistening orb of aqueous torment,"
    " sapping life with each passing moment.", "Spell", "Trap",randint(1, 3), 1, 1, 0)

Spell("Bombarda Maxima", "Conjures a cataclysmic blast, scattering the ashes of the fallen.",
      "Spell", "Offensive", randint(20, 45), 1, 0.8, 0)

Spell("Accio", "Drags that which is distant into the grasp of the conjurer.",
      "Charm", "Trap", randint(1, 5), 1, 1, 0)

Spell("Episkey", "Mends the frayed sinews and cracked bones of the caster.",
      "Charm", "Heal", randint(5, 10), 1, 1, 0)

Spell("Protego", "Erects a fleeting bastion against incoming malice.",
      "Charm", "Defensive", randint(2, 7), 1, 1, 0)

Spell("Mana increase #1", "Augments the caster's inner reservoir of arcane essence by a paltry measure.",
      "Charm", "Passive", 10, 1, 1, 0)

Spell("Expecto Patronum", "Summons a spectral ward, a bulwark against the encroaching dark.",
      "Charm", "Defensive",randint(2, 5), 2, 0.8, 0)

Spell("Protego Horribilis", "Conjures a formidable ward, a stout defense against the abyss.",
      "Charm", "Defensive",randint(10, 20), 5, 0.7, 0)

Spell("Protego Maxima", "Calls forth an indomitable barrier of shimmering light, a fortress against the onslaught of the void.",
      "Charm", "Defensive", randint(60, 100), 10, 0.6, 0)

Spell("Mana increase #2", "Broadens the caster's arcane cistern, flooding it with greater potential.",
      "Charm", "Passive", 20, 15, 0.9, 0)

Spell("Mana increase #3", "Enlarges the vessel of the soul, granting a vast surge of ethereal energy.",
      "Charm", "Passive", 30, 20, 0.8, 0)

Spell("Mana increase #4", "Expands the threshold of mortal magic, ushering a torrent of raw power.",
      "Charm", "Passive", 35, 25, 0.7, 0)

Spell("Mana increase #5", "Increases maximum mana for 40.", "Charm", "Passive",40,
      30, 0.6, 0)

Spell("Impedimenta", "Encumbers the foe with invisible chains, halting their wretched advance.",
      "Jinx", "Trap", randint(2, 4), 4, 0.7, 0)

Spell("Sectumsempra", "Lacerates the flesh with unseen blades, leaving grievous, bleeding scars.",
      "Curse", "Offensive", 300, 20, 0.3, 0)

Spell("Imperio", "Enthralls the will of the feeble-minded, binding their soul to the caster's whim.",
      "Curse", "Offensive", randint(4, 7), 30, 0.25, 0)

Spell("Confringo", "Ignites the very essence of the foe, causing them to erupt in a cascade of ruin.",
      "Curse", "Offensive", 600, 40, 0.2, 0)

Spell("Avada Kedavra", "Extinguishes the flickering flame of life with a whisper of absolute finality.",
      "Curse", "Offensive",1000, 50, 0.15, 0)

