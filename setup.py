from setuptools import find_packages, setup

setup(
        name='sessionprofile',
        version='1.0',
        packages=find_packages(),
        package_dir = {'': 'django/sessionprofile'},

        platforms=['any'],
)
