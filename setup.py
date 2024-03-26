from setuptools import find_packages, setup

setup(
    name='netbox-discrepancy',
    version='0.1',
    description='A plugin to show discrepancies between NetBox and the real world',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
