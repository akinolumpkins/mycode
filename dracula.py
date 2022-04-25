#!/usr/bin/env python3

counter= 0

with open("345-0.txt","r") as foo:
    for line in foo:
        print if "vampire" in line.lower():
            print(line)
            counter += 1
print(counter)

