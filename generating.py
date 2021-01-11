# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is for generating numbers

import random

generating = random.randint(1, 100)


def main():
    
    random_list = []

    for loop_counter in range(1,10+1):
        randoms = generating
        random_list.append(randoms)
    print("")
    
    for loop_counter in range(1,10+1):
        average = random_list[loop_counter]
        

if __name__ == "__main__":
    main()
