[![Build Status](https://travis-ci.org/Accelize/ansible-role-linux-kernel.svg?branch=master)](https://travis-ci.org/Accelize/ansible-role-ansible-drm)

Linux Kernel Role
=================

This Ansible role install ans enable a specific kernel version from OS repositories.

Requirements
------------

The role requires to be run as root on the target host.

The system requires to be rebooted to apply the kernel change.

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

  tasks:
    # Reboot to apply the kernel change
    - name: Ensure system is rebooted
      reboot:
    # If kernel version is required in a following step, update facts to get
    # the new kernel version
    - name: Ensure Ansible facts are up to date
      setup:

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
