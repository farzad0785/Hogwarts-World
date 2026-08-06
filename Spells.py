from random import randint


class Spell:
    spell = {"level 1": {"Bombarda": {"description": "Creates a small explosion. ",
                                      "amount": randint(5, 15),
                                      "learning chance": 1
                                      },
                         "Deprimo":{"description": "A spell that places immense pressure on a target, causing it to collapse or explode.",
                                    "amount": randint(1, 10),
                                    "learning chance": 1,
                                    },
                         "Ebublio": {"description": "Causes a target to become trapped in a large bubble. Takes damage each round. ",
                             "amount": randint(1, 3),
                             "learning chance": 1
                             },

                         },
              "level 2": {"Bombarda Maxima": {"description": "Creates a large, powerful explosion.",
                                              "amount": randint(20, 45),
                                              "learning chance": 0.8,
                                              },
                          },
             }
    charm = {"level 1": {"Accio": {"description": "Summons an object to the caster. ",
                                   "amount": randint(1, 5),
                                   "learning chance": 1
                                   },
                         "Episkey":{"description": "Heals minor injuries",
                                    "amount": randint(5, 10),
                                    "learning chance":1,
                                    },

                         "Protego":{"description": "The Shield Charm. ",
                                    "amount": randint(2, 7),
                                    "learning chance": 1
                                    },
                         "Mana increase #1":{"description": "Increases maximum mana for 10.",
                                             "amount": 10,
                                             "learning chance": 1
                                             },

                         },
              "level 2": {"Expecto Patronum":{"description": "Conjures a spirit guardian to protect against Enemies.",
                                              "amount": randint(2, 5),
                                              "learning chance":0.8,
                                              },
                          },
              "level 5": {"Protego Horribilis": {"description": "A powerful protective spell. ",
                                                "amount": randint(10, 20),
                                                "learning chance": 0.7,
                                                },
                         },
              "level 10": {"Protego Maxima": {"description": "An advanced shield charm that creates a large, powerful defensive barrier.",
                                              "amount": randint(60, 100),
                                              "learning chance": 0.6
                                              },
                           },
              "level 15": {"Mana increase #2":{"description": "Increases maximum mana for 20.",
                                              "amount": 20,
                                              "learning chance": 0.9
                                              },
                          },
              "level 20": {"Mana increase #3":{"description": "Increases maximum mana for 30.",
                                              "amount": 30,
                                              "learning chance": 0.8
                                              },},
              "level 25": {"Mana increase #4":{"description": "Increases maximum mana for 35.",
                                              "amount": 35,
                                              "learning chance": 0.7
                                              },
                          },
              "level 30": {"Mana increase #5":{"description": "Increases maximum mana for 40.",
                                              "amount": 40,
                                              "learning chance": 0.6
                                              },
                          }
             }
    hex = {}
    jinx = {"level 1": {},
              "level 2": {},
              "level 3": {},
              "level 4": {},
              "level 5": {}}
    curse = {"level 10": {},
              "level 20": {"Sectumsempra": {"description": "A dark curse that inflicts deep, razor-like wounds on the target.",
                                            "amount": 0.6}},
              "level 30": {"Imperio": {"description": "The Imperius Curse, which places the target under the caster’s complete control.",
                                       "amount": randint(4, 7)},
                                       "learning chance": 0.3
                           },
              "level 40": {"Confringo": {"description": "A blasting curse that causes the target to explode.",
                                         "amount": 0.8,
                                         "learn chance": 0.2,
                                         }
                           },
              "level 50": {"Avada Kedavra":{"description": "The Killing Curse, which causes instant death.",
                                            "amount": 1000,
                                            "learning chance": 0.1,
                                            },
                           },
             }