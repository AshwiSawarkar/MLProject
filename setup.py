from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirenments for the project like packages and all 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name="MlProject",
version='0.0.1',
author='AshwiniSSawarkar',
author_email='ashwi1987@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)