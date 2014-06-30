ansible-wrapper
===============

For ansible users with large scale inventory systems.

#### use cases

* if you have a large number of machines and returning all of your cluster information for every ansible invocation doesn't make sense.

* you are using a cloud provider and there isn't already a dynamic inventory script (like ec2) so you've written your own, but you want to scope responses to specific clusters.

#### why this wrapper?

as outlined in [http://docs.ansible.com/developing_inventory.html](http://docs.ansible.com/developing_inventory.html), your dynamic inventory script is expected to output basically every cluster and host in your entire infrastructure, then it will match based on the host-pattern you supplied to ansible. This can be problematic when you have tens of thousands of hosts.

with this wrapper, you can set environment variables (ANSIBLE_QUERY and ANSIBLE_QUERY_TYPE) that will scope your dynamic inventory scripts' response to only the machines you care about. additionally, it will parse the 'hosts' section of your playbooks to do the same.

#### how?

create an alias for the wrapper

    alias ansible="/path/to/ansible-wrapper.py ansible"
    alias ansible-playbook="/path/to/ansible-wrapper.py ansible-playbook"

Notice there is a unique alias for `ansible` and `ansible-playbook`.
If you invoke `ansible`, the wrapper will set the environment variable "ANSIBLE_QUERY" to the host-pattern you supplied to ansible, while also setting "ANSIBLE_QUERY_TYPE" to 'host-pattern'. Make sure your dynamic inventory script reads these vars.

for example: `ansible %prod.service -m ping` will set `ANSIBLE_QUERY="%prod.service"` and `ANSIBLE_QUERY_TYPE="host-pattern"`

for playbooks, it will set the ANSIBLE_QUERY_TYPE environment var to 'playbook', and then set the ANSIBLE_QUERY to the list of playbook files. Your dynamic inventory script should then read these yaml files and scope it's response based on what is set in the 'hosts' line of your playbook yamls.

#### enjoy

Feel free to open up issues/PR's 
