'''
 The setup.py file is an essential part of packaging and 
 distributing Python projects . It is used by setuptools(or distuils in older Python versions)
  to define the configuration of your Project, such as its metadata, dpedencises and more
'''

from setuptools import find_packages,setup #rersponsible for providing all the information regarding the projects
from typing import List

def get_requirements()->List[str]:
    '''
     This function will return List of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement !='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst 

print(get_requirements())


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Krish Naik",
    author_email="mdinamulh04@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)