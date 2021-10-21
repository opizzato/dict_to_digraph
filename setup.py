from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="dict_to_digraph",
    version="0.0.3",
    author="Olivier Pizzato",
    author_email="olivier.pizzato@gmail.com",
    description="Turn python dictionary into Graphviz digraph",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/opizzato/dict_to_digraph",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
