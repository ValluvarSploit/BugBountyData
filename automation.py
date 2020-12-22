#!/usr/bin/python3

domains_local_list = []
domains_remote_list = []
wildcard_local_list = []
wildcard_remote_list = []

with open('domains.txt', 'r') as domains_remote_file:
    for line in domains_remote_file:
        domains_remote_list.append(line.strip())

with open('domains-local.txt', 'r') as domains_local_file:
    for line in domains_local_file:
        domains_local_list.append(line.strip())

for element in domains_remote_list:
    if element not in domains_local_list:
        with open('domains-output.txt', 'a') as domain_output:
            domain_output.write(element)
            domain_output.write('\n')


with open('wildcards.txt', 'r') as wildcards_remote_file:
    for line in wildcards_remote_file:
        wildcard_remote_list.append(line.strip())

with open('wildcard-local.txt', 'r') as wildcard_local_file:
    for line in wildcard_local_file:
        wildcard_local_list.append(line.strip())

for element in wildcard_remote_list:
    if element not in wildcard_local_list:
        with open('wildcard-output.txt', 'a') as wildcard_output:
            wildcard_output.write(element)
            wildcard_output.write('\n')
