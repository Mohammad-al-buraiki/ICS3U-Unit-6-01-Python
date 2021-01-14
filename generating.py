# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is for generating numbers

import random


def main():
    random_list = []
    number_of_elements = 10

    for loop_counter in range(0, number_of_elements):
        generating = random.randint(1, 100)
        random_list.append(generating)
        print(generating)

    print("")

    total = 0
    for loop_counter in range(0, number_of_elements):
        total = total + random_list[loop_counter]

    average = total / number_of_elements
    print("The total is: {0}.".format(total))
    print("The average is {0}.".format(average))


if __name__ == "__main__":
    main()
