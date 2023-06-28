from setuptools import find_packages, setup
#from typing import List

def get_requirments():
    requirements:list(str) = []
    with open('requirements.txt', 'r') as f:
        reqContent = f.readlines()
        for line in reqContent:
            if line != '-e .' :
                requirements.append(line)
    return requirements

setup(
    name = "Sensor",
    version = "0.0.1",
    author = "anu-katiyar18",
    author_email="anuradha.katiyar@gmail.com",
    packages = find_packages(),
    install_requires = get_requirments(),
)