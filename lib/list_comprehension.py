#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for i in num_list:
        if i%2 == 0:
            evens.append(i)
    # for i in num_list:
    #     num_list.remove(i%2 != 0)
    print(evens)

return_evens([0, 1, 3, 5, 7, 8, 9])

def make_exclamation(sentence_list):
    exclamation = "!"
    final_list = [i + exclamation for i in sentence_list]

    # for i in sentence_list:
    #     final_list.append(i + exclamation)
    print(final_list)


make_exclamation(["Hello", "I'm doing great", "Python is fun"])