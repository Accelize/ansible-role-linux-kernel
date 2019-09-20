[![Build Status](https://travis-ci.org/Accelize/ansible-role-linux-kernel.svg?branch=master)](https://travis-ci.org/Accelize/ansible-role-ansible-drm)

Linux Kernel Role
=================

This Ansible role install ans enable a specific kernel version from OS repositories.

Requirements
------------

The role requires to be run as root on the target host.

The specified Kernel version must be supported by OS repositories (This include "Vault" repositories for Red hat based distributions).

Role Variables
--------------

* **install_kernel_headers**: If True, also install matching kernel headers. Default to `true`.
* **kernel_version**: Install the most recent kernel version available that start by this value. Default to `''`.

Example Playbook
----------------

```yaml
- hosts: servers
  become: true  
  roles:
     - role: accelize.linux_kernel
  vars:
     kernel_version: 3.10.0-693
```

Dependencies
------------

None.

License
-------

Apache 2.0

Author Information
------------------

This role is provided by [Accelize](https://www.accelize.com).
