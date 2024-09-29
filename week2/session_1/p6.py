global_dict = {"A" : 4, "B": 3, "C" : 2, "D" : 1, "F" : 0  }


def calculate_gpa(report_card):
    #take report card's values 
    # compare the card's values and global_dict's keys 
    # get the values of global_dict keys
    #then do the computation
    sum = 0
    for grade in report_card.values():
        if grade in global_dict.keys():
            sum += global_dict[grade]
    average_gpa = sum / len(report_card)
    return average_gpa


def main():
    report_card = {"Math": "B", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
    print(calculate_gpa(report_card))

main()

