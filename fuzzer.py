#!/usr/bin/env python

import sys,requests,concurrent.futures


def fuzzer(sub_domains):
    
    print('------------------starting subdomain enumeration----------------------')
    for sub in sub_domains:
        sub_domain = f"http://{sub}.{sys.argv[1]}"

        try:
            response = requests.get(sub_domain)

        except requests.ConnectionError:
            pass

        else:
            print(sub_domain, '  ', '[ Status code:', response.status_code,']')


if __name__='__main__':

    sub_list = open(sys.argv[2]).read()
    sub_domains = sub_list.splitlines()

    fuzzer(sub_domains)
