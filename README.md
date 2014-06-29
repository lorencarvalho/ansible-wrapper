ansible-wrapper
===============

simple python wrapper for ansible to pass additional arguments to your dynamic inventory script

as outlined in http://docs.ansible.com/developing_inventory.html, your dynamic inventory script is expected to output basically every cluster and host in your entire infrastructure, then it will match based on the host-pattern you supplied to ansible. This can be problematic when you have tens of thousands of hosts.

with this wrapper, you can set environment variables that will scope your dyn inventory scripts response to only the machines you care about. additionally, it will parse the 'hosts' section of your playbooks to do the same.

enjoy
