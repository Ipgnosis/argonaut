from setuptools import setup, find_packages

setup(
    name="colchis",  # The name on PyPI (must be unique)
    version="0.1.0",  # Your package's version
    packages=find_packages(),  # Automatically find packages within your project
    authors = [
    { name="Russell Bennett", email="russell@ipgnosis.com" },
    ]
    description = "A package, implemented as a Class, to generalize JSON traversal and processing."
    readme = "README.md"
    requires-python = ">=3.8"
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ]

    [project.urls]
    Homepage = "https://github.com/Ipgnosis/argonaut"
    Issues = "https://github.com/Ipgnosis/argonaut/issues")
