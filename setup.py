'''
The setup.py file is an essential part of the packageing and 
distibuting python projects. It is used by setuptools 
(or distutils in older python versions) to define the configuration 
of the project, such as its metadata, dependencies, and more.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return a list of requirements from the requirements.txt file
    '''
    requirement_list:List[str] = []
    try:
        with open("requirements.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found")

    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Rahul",
    author_email="rahul@abc.com",
    packages=find_packages(),
    install_requires=get_requirements()
)