

def highest_rated(books):
    rating = 0
    highest_rated_book = None
    #iterate over the items in a list:
    #and iterate over the ratings item in a dictionary
    #store the ratings numbers in an empty list
    #find the largest rating number using max()
    #return that specific element with highest rating number 

    for book in books:
        if book["rating"] > rating:
            rating = book["rating"]
            highest_rated_book = book
    return highest_rated_book
        
            
def main():
    books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }]

    print(highest_rated(books))


main()
