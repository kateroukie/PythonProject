def permutation(listy):
    if len(listy) == 0:
        print("Empty Word Error!")
        return []
    elif len(listy) == 1:
        return [listy]
    else:
        new_list = []
        if not repetition:
            listy = list(set(listy))
        for i in range(len(listy)):
            m = listy[i]
            rest_word = listy[:i] + listy[i + 1:]
            for perm in permutation(rest_word):
                new_list.append([m] + perm)
        return new_list


if __name__ == '__main__':
    print("Enter yes if you prefer permutations with repetition, otherwise enter no. ")
    if input() == "yes":
        repetition = True
    else:
        repetition = False
    word = input("Enter the word: ")
    data = list(word)
    final_set = set()
    for perm in permutation(data):
        final_set.add("".join(perm))
    for word in final_set:
        print(word)

