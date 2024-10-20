"""Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.

The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.

Hint: To test, loop over Pokemon in return list and print the Pokemon's name"""

class Pokemon():
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
    def __str__(self):
        return f"Pokemon(name={self.name}, types={self.types}, is_caught={self.is_caught})"

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
	
    def catch(self):
        self.is_caught = True
		
    def choose(self):
        if self.is_caught == True:
            print(f"{self.name} I choose you")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)

def get_by_type(my_pokemon, pokemon_type):
    type_list = []
    for pokemon in my_pokemon:
         if pokemon_type in pokemon.types:
             type_list.append(pokemon.name)
    return type_list
            


def main():
    jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
    diglett = Pokemon("Diglett", ["Ground"])
    meowth = Pokemon("Meowth", ["Normal"])
    pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
    blastoise = Pokemon("Blastoise", ["Water"])

    my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
    normal_pokemon = get_by_type(my_pokemon, "Normal")
    print(normal_pokemon)

main()
