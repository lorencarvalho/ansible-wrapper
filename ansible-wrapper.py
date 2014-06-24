#!/usr/bin/env python
'''
python wrapper for executing ansible and passing the host-pattern to
your dynamic inventory script as an argument

have your dynamic inventory script read the env vars
that are set by this script to scope the response to
only the hosts you want to work on.

in your .bashrc put:
alias ansible="/path/to/this/script ansible"
alias ansible-playbook="/path/to/this/script ansible-playbook"

todo:
    exit cleanly on ctrl-c
    better conditional logic
'''

import sys
import os
import shlex
from subprocess import call


def ansible(args):
    try:
        os.environ['ANSIBLE_QUERY_TYPE'] = 'host-pattern'
        os.environ['ANSIBLE_QUERY'] = args[2]
    except:
        pass


def ansible_playbook(args):
    playbooks = []
    try:
        for arg in args[2:]:
            if arg.startswith('-'):
                break
            else:
                playbooks.append(arg)
        os.environ['ANSIBLE_QUERY_TYPE'] = 'playbook'
        os.environ['ANSIBLE_QUERY'] = ' '.join(playbooks)
    except:
        pass


def main():
    try:
        args = sys.argv
        # move args back until host-pattern or playbooks are found
        while args[2].startswith('-'):
            pass_back = [args.pop(2), args.pop(2)]
            args = args + pass_back

        # set appropriate env vars
        if args[1] == 'ansible':
            ansible(args)
        elif args[1] == 'ansible-playbook':
            ansible_playbook(args)

        # execute!
        call(shlex.split(' '.join(args[1:])))
    except KeyboardInterrupt:
        sys.exit('got ctrl-c')

if __name__ == '__main__':
    main()
