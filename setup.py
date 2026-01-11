from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path)->List[str]:
    '''This function will return the list of requirements/packages'''
    with open(file_path) as f:
        requirements = f.readlines()
#    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="MLproject",
    version="0.0.1",
    author="Vidit",
    author_email="viditsaxena81@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)