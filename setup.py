import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sports",
    version="0.0.0",
    author="David Scott Orkin",
    author_email="orange.cardinal.technology@gmail.com",
    description="APIs for gathering data from professional sport websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OrangeCardinal/sports",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)