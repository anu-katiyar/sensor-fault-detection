from setuptools import find_packages, setup
#from typing import List

def get_requirments():
    requirements:list(str) = []
    with open('requirements.txt', 'r') as f:
        reqContent = f.readline()
        for line in reqContent:
            requirements.append(line.strip())
    return requirements

setup(
    name = "Sensor",
    version = "0.0.1",
    author = "anu-katiyar18",
    author_email="anuradha.katiyar@gmail.com",
    packages = find_packages(),
    install_requires = get_requirments(),
)