def match_made(dictionary):
	for key, value in dictionary.items():
		print( f"{key} and {value} are a perfect match.")
		

def main():
	dictionary = {"Peanut Butter" : "Jelly", "Spongebob": "Patrick", "Ash": "Pikachu"}
	# Peanut butter and Jelly are a perfect match.
    # Spongebob and Patrick are a perfect match.
    # Ash and Pikachu are a perfect match.
	(match_made(dictionary))

main()