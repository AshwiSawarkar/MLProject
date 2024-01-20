from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirenments for the project like packages and all 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.rplace("\n","") for req in requirements]


setup(
name="Mlroject",
version='0.0.1',
author='AshwiniSSawarkar',
author_email='ashwi1987@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)