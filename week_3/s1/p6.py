
def min_distance(words, word1, word2):
    min_dist = len(words)  # Initialize with a large value
    index1, index2 = None, None

    for i, word in enumerate(words):
        if word == word1:
            index1 = i
        elif word == word2:
            index2 = i

        if index1 is not None and index2 is not None:
            min_dist = min(min_dist, abs(index1 - index2))

    return min_dist

         
def main():
    words = ["the", "quick", "brown", "fox", "jumped", "the"]
    dist1 = min_distance(words, "quick", "jumped")
    dist2 = min_distance(words, "the", "jumped")
    print(dist1)
    print(dist2)

    words2 = ["code", "path", "code", "contribute",  "practice"]
    dist3 = min_distance(words2, "code", "practice")
    print(dist3)

main()

