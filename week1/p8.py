def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score >21:
        print("Bust!")
    elif score>= 17 and score <21:
        print("nice hand!")
    else:
        print("Hit me!")

blackjack(13)
blackjack(28)
blackjack(21)
blackjack(1)


# If score equals 21, print "Blackjack!".
# If score is greater than 21, print "Bust!".
# If score is greater than or equal to 17 and less than 21, print "Nice hand!".
# If score is less than 17, print "Hit me!".
