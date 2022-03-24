from setuptools import setup, find_packages

requirements = []
with open("requirements.txt") as r:
    requirements = r.read().splitlines()

readme = ""
with open("README.md") as f:
    readme = f.read()

setup(
    name="rocketman",
    author="Juan Ignacio Battiston",
    author_email="juani.battiston2002@gmail.com",
    url="https://github.com/Batucho/Rocketman",
    project_urls={},
    version="0.1.0",
    packages=find_packages(),
    license="MIT",
    description="An API wrapper for the r/SpaceX API",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.9.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
