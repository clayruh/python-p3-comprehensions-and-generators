#!/usr/bin/env python3

def return_evens(num_list):
    return [i for i in num_list if i%2 == 0]
    # for i in num_list:
    #     if i%2 == 0:
    #         evens.append(i)
    # print(evens)

# return_evens([1, 10, 2])

def make_exclamation(sentence_list):
    exclamation = "!"
    return [i + exclamation for i in sentence_list]

    # for i in sentence_list:
    #     final_list.append(i + exclamation)
    # print(final_list)


# make_exclamation(["Hello", "I'm doing great", "Python is fun"])
