from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    HYPHEN_E='-e .'
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
    return requirements


setup(name='mlproject',
      version='0.0.1',
      author='AyorindeAlase',
      author_email='alaseayorinde@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')


)