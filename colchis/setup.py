from setuptools import setup, find_packages

setup(
    name="colchis",
    version="0.1.0",
    packages=find_packages(),
    author="Russell Bennett",
    author_email="russell@beanbazaar.com",
    description="A package, implemented as a Class, to generalize JSON traversal and processing.",
    long_description=open("../README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license_files=('../LICENSE.txt'),
    project_urls={
        "Homepage": "https://github.com/Ipgnosis/colchis",
        "Issues": "https://github.com/Ipgnosis/colchis/issues",
    }
)
