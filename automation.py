#!/usr/bin/python3

file1 = []
file2 = []

with open('domains.txt', 'r') as f1:
    for line in f1:
        file1.append(line.strip())

with open('domains2.txt', 'r') as f2:
    for line in f2:
        file2.append(line.strip())

for element in file1:
    if element not in file2:
        #print(element)
        with open('output.txt', 'a') as output:
            output.write(element)
            output.write('\n')
