#!/usr/bin/python3

domains_local_list = []
domains_remote_list = []
#wildcard_local_list = []
#wildcard_remote_list = []

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
