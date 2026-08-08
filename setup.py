from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''this function will return list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.strip() for req in requirements]  #there will be packeges written one by one in different lines so 
        # requirements= file_obj.readlines() , this will also read \n that is why we replaced "\n" with ""
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='ml-project',
    version='0.0.1',
    author='unnati bohare',
    author_email='palakbohare@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
# whenever i am trying to install these packages from requirements.txt my setup.py should also run at that time so # it will automatically trigger setup.py