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
'''

import argparse
import os


def ansible(args):
    try:
        os.environ['ANSIBLE_QUERY_TYPE'] = 'host-pattern'
        os.environ['ANSIBLE_QUERY'] = args[1]
    except:
        pass


def ansible_playbook(args):
    playbooks = []
    try:
        for arg in args[1:]:
            if arg.startswith('-'):
                break
            else:
                playbooks.append(arg)
        os.environ['ANSIBLE_QUERY_TYPE'] = 'playbook'
        os.environ['ANSIBLE_QUERY'] = ' '.join(playbooks)
    except:
        pass


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_known_args()
    args = args[1]

    # check if any args were passed (or --version or what-have-you)
    if not args:
        raise SystemExit
    elif len(args) <=2:
        os.execvp(args[0], args)
    # some basic envs
    os.environ['ANSIBLE_HOST_KEY_CHECKING'] = "False"
    os.environ['ANSIBLE_SSH_ARGS'] = ""
    try:
        # move args back until host-pattern or playbooks are found
        allowed_first_args = ['-h', '-v', '-K', '-k', '-C', '-o', '-S', '-s']
        while args[1].startswith('-'):
            if len(args) % 2 == 0:
                pass_back = [args.pop(1), args.pop(1)]
                args = args + pass_back
            elif args[1] in allowed_first_args:
                pass_back = [args.pop(1)]
                args = args + pass_back

        # set appropriate env vars
        if args[0] == 'ansible':
            ansible(args)
        elif args[0] == 'ansible-playbook':
            ansible_playbook(args)

        # exec!
        os.execvp(args[0], args)
    except KeyboardInterrupt:
        raise SystemExit


if __name__ == '__main__':
    main()
