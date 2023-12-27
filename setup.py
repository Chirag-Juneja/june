from setuptools import find_packages, setup

setup(
    name="june",
    version="0.0.1",
    description="A simple machine learning framework",
    package_dir={"":"june"},
    packages=find_packages(where="june"),
    author='Chirag Juneja', 
    author_email='chiragjuneja6@gmail.com', 
)