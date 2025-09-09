from setuptools import find_packages, setup

setup(
    name = "iit-madras-bot",
    version = "0.0.0",
    author = "Niloy Mondal",
    author_email="syphonop@gmail.com",
    description="A chatbot for IIT Madras BS program",
    packages=find_packages(where="src"),
    install_requires=[]
)