class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

def main():
    my_pokemon = Pokemon("Pikachu", "Electric")
    print (my_pokemon.name)

main()