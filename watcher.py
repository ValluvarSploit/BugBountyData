#!/usr/bin/python3
import os

os.system('touch domains-new.txt')
os.system('touch wildcards-new.txt')

domains_local_list = []
domains_remote_list = []
wildcards_local_list = []
wildcards_remote_list = []

with open('domains.txt', 'r') as domains_remote_file:
    with open('wildcards.txt', 'r') as wildcards_remote_file:
        with open('domains-local.txt', 'r') as domains_local_file:
            with open('wildcards-local.txt', 'r') as wildcard_local_file:
                for drline in domains_remote_file:
                    domains_remote_list.append(drline.strip())
                for wrline in wildcards_remote_file:
                    wildcards_remote_list.append(wrline.strip())
                for dlline in domains_local_file:
                    domains_local_list.append(dlline.strip())
                for wlline in wildcard_local_file:
                    wildcards_local_list.append(wlline.strip())

for element in domains_remote_list:
    if element not in domains_local_list:
        with open('domains-new.txt', 'a') as df:
            df.write(element)
            df.write('\n')

for element in wildcards_remote_list:
    if element not in wildcards_local_list:
        with open('wildcards-new.txt', 'a') as wf:
            wf.write(element)
            wf.write('\n')