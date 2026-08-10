from random import randint


class Spell:
    spell = {
        "Bombarda": {
            "description": "Unleashes a paltry burst of ruinous fire.",
            "amount": randint(5, 15),
            "required level": 1,
            "learning chance": 1,
            },
            "Deprimo": {
                "description": "Crushing weight descends upon the foe, rending flesh and bone to shards.",
                "amount": randint(1, 10),
                "required level": 1,
                "learning chance": 1,
                },
            "Ebublio": {
                "description": "Traps the hapless soul within a glistening orb of aqueous torment, sapping life with each passing moment.",
                "amount": randint(1, 3),
                "required level": 1,
                "learning chance": 1
                },
            "Bombarda Maxima": {
                "description": "Conjures a cataclysmic blast, scattering the ashes of the fallen.",
                "amount": randint(20, 45),
                "required level": 1,
                "learning chance": 0.8,
                },
        }
    charm = {
        "Accio": {
            "description": "Drags that which is distant into the grasp of the conjurer.",
            "amount": randint(1, 5),
            "required level": 1,
            "learning chance": 1
            },
        "Episkey": {
            "description": "Mends the frayed sinews and cracked bones of the caster.",
            "amount": randint(5, 10),
            "required level": 1,
            "learning chance":1,
            },
        "Protego":{
            "description": "Erects a fleeting bastion against incoming malice.",
            "amount": randint(2, 7),
            "required level": 1,
            "learning chance": 1
            },
        "Mana increase #1":{
            "description": "Augments the caster's inner reservoir of arcane essence by a paltry measure.",
            "amount": 10,
            "required level": 1,
            "learning chance": 1
            },
        "Expecto Patronum": {
            "description": "Summons a spectral ward, a bulwark against the encroaching dark.",
            "amount": randint(2, 5),
            "required level": 2,
            "learning chance":0.8,
            },
        "Protego Horribilis": {
            "description": "Conjures a formidable ward, a stout defense against the abyss.",
            "amount": randint(10, 20),
             "required level": 5,
            "learning chance": 0.7,
            },
        "Protego Maxima": {
            "description": "Calls forth an indomitable barrier of shimmering light, a fortress against the onslaught of the void.",
            "amount": randint(60, 100),
            "required level": 10,
            "learning chance": 0.6
            },
        "Mana increase #2": {
                  "description": "Broadens the caster's arcane cistern, flooding it with greater potential.",
                  "amount": 20,
                  "required level": 15,
                  "learning chance": 0.9
                  },
        "Mana increase #3": {
            "description": "Enlarges the vessel of the soul, granting a vast surge of ethereal energy.",
            "amount": 30,
            "required level": 20,
            "learning chance": 0.8
            },
        "Mana increase #4": {
            "description": "Expands the threshold of mortal magic, ushering a torrent of raw power.",
            "amount": 35,
            "required level": 25,
            "learning chance": 0.7
            },
        "Mana increase #5": {
            "description": "Increases maximum mana for 40.",
            "amount": 40,
            "required level": 30,
            "learning chance": 0.6
            },
    }

    jinx = {
        "Impedimenta": {
            "description": "Encumbers the foe with invisible chains, halting their wretched advance.",
            "amount": randint(2, 4),
            "required level": 4,
            "learning chance": 0.7,
            },
    }

    curse = {
        "Sectumsempra": {
            "description": "Lacerates the flesh with unseen blades, leaving grievous, bleeding scars.",
            "amount": 0.6,
            "required level": 20,
            "learning chance": 0.3,
            },

        "Imperio": {
             "description": "Enthralls the will of the feeble-minded, binding their soul to the caster's whim.",
             "amount": randint(4, 7),
             "required level": 30,
             "learning chance": 0.25,
             },

        "Confringo": {
             "description": "Ignites the very essence of the foe, causing them to erupt in a cascade of ruin.",
             "amount": 0.8,
             "required level": 40,
             "learning chance": 0.2,
             },
        "Avada Kedavra": {
             "description": "Extinguishes the flickering flame of life with a whisper of absolute finality.",
             "amount": 1000,
             "required level": 50,
             "learning chance": 0.15,
             },
    },