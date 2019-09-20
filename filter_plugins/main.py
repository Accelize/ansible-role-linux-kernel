"""Extra Ansible filters"""


def _rhel_kernel_info(packages, kernel_version, *_, **__):
    """
    Return kernel and associated repository.

    Args:
        packages (dict): DNF/YUM list output.
        kernel_version (str): Kernel version to install.

    Returns:
       dict: kernel version, repository
    """
    kernels = list()

    # List all available kernel version and associated repository
    for line in packages['stdout'].splitlines():
        if line.startswith('kernel.') and not line.startswith('kernel.src'):
            yum_package = line.strip().split()
            kernels.append(dict(version=yum_package[1], repo=yum_package[2]))

    # Return more recent kernel version that match version requirement
    for kernel in reversed(kernels):
        if kernel['version'].startswith(kernel_version):
            return kernel

    raise RuntimeError(
        'No kernel matching to "%s". Available kernel versions: %s' % (
            kernel_version,
            ', '.join(kernel['version'] for kernel in kernels)))


def rhel_kernel(packages, kernel_version, *_, **__):
    """
    Return matching kernel version.

    Args:
        packages (dict): DNF/YUM list output.
        kernel_version (str): Kernel version to install.

    Returns:
       str: kernel version.
    """
    return _rhel_kernel_info(packages, kernel_version)['version']


def rhel_repo(packages, kernel_version, *_, **__):
    """
    Return repository where found specified kernel version.

    Args:
        packages (dict): DNF/YUM list output.
        kernel_version (str): Kernel version to install.

    Returns:
       str: repository name
    """
    return _rhel_kernel_info(packages, kernel_version)['repo']


class FilterModule(object):
    """Return filter plugin"""

    @staticmethod
    def filters():
        """Return filter"""
        return {'rhel_kernel': rhel_kernel, 'rhel_repo': rhel_repo}
