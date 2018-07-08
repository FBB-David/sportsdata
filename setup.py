import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sportsdata",
    version="0.0.1",
    author="David Scott Orkin",
    author_email="orange.cardinal.technology@gmail.com",
    description="APIs for gathering data from professional sport websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OrangeCardinal/sportsdata",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)