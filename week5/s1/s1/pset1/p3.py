class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })

def main():
    squirtle = Pokemon("Squirtle", "Water")
    squirtle.print_pokemon()
    squirtle.is_caught = True
    squirtle.print_pokemon()

main()