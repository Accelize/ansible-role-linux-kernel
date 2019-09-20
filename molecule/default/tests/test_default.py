import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages_installed(host):
    """
    Test that packages are installed
    """
    installed = False
    for name in ("kernel", "kernel-common",
                 "kernel-devel", "kernel-headers", "linux-headers"):
        package = host.package(name)
        if not package.is_installed:
            continue
        assert f'{package.version}-{package.release}'.startswith(
            host.ansible.get_variables().get('kernel_version', ''))
        installed = True

    if not installed:
        raise RuntimeError('No kernel package found')
